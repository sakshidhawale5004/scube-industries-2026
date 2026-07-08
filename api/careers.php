<?php
// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Set response header
header('Content-Type: application/json');

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Get form data
$fullName = isset($_POST['fullName']) ? trim($_POST['fullName']) : '';
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
$phone = isset($_POST['phone']) ? trim($_POST['phone']) : '';
$location = isset($_POST['location']) ? trim($_POST['location']) : '';
$position = isset($_POST['position']) ? trim($_POST['position']) : '';

// Validate required fields
if (empty($fullName) || empty($email) || empty($phone) || empty($location) || empty($position)) {
    http_response_code(400);
    echo json_encode(['error' => 'Missing required fields']);
    exit;
}

// Validate email format
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid email address']);
    exit;
}

// Handle file upload
$resumeAttachment = '';
$resumeFileName = '';

if (isset($_FILES['resume']) && $_FILES['resume']['error'] === UPLOAD_ERR_OK) {
    $uploadDir = 'uploads/resumes/';
    
    // Create directory if it doesn't exist
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0755, true);
    }
    
    $fileName = $_FILES['resume']['name'];
    $fileTmp = $_FILES['resume']['tmp_name'];
    $fileSize = $_FILES['resume']['size'];
    $fileType = $_FILES['resume']['type'];
    
    // Validate file
    $allowedTypes = ['application/pdf'];
    $maxSize = 5 * 1024 * 1024; // 5MB
    
    if (!in_array($fileType, $allowedTypes)) {
        http_response_code(400);
        echo json_encode(['error' => 'Only PDF files are allowed']);
        exit;
    }
    
    if ($fileSize > $maxSize) {
        http_response_code(400);
        echo json_encode(['error' => 'File size must be less than 5MB']);
        exit;
    }
    
    // Generate unique filename
    $uniqueFileName = time() . '_' . basename($fileName);
    $uploadPath = $uploadDir . $uniqueFileName;
    
    if (move_uploaded_file($fileTmp, $uploadPath)) {
        $resumeFileName = $uniqueFileName;
        $resumeAttachment = $uploadPath;
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to upload resume']);
        exit;
    }
}

// Admin email address
$adminEmail = 'sales@scubeindustries.com';

// Prepare email to admin
$adminSubject = "New Career Application: " . $position;
$adminMessage = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background-color: #02204c; color: white; padding: 20px; border-radius: 5px 5px 0 0; }
        .content { background-color: #f9f9f9; padding: 20px; border: 1px solid #ddd; }
        .field { margin-bottom: 15px; }
        .label { font-weight: bold; color: #02204c; }
        .value { color: #555; margin-top: 5px; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>New Career Application</h2>
        </div>
        <div class='content'>
            <div class='field'>
                <div class='label'>Name:</div>
                <div class='value'>" . htmlspecialchars($fullName) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Email:</div>
                <div class='value'>" . htmlspecialchars($email) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Phone:</div>
                <div class='value'>" . htmlspecialchars($phone) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Location:</div>
                <div class='value'>" . htmlspecialchars($location) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Position Applied For:</div>
                <div class='value'>" . htmlspecialchars($position) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Resume:</div>
                <div class='value'>See attached file</div>
            </div>
        </div>
    </div>
</body>
</html>
";

// Prepare auto-reply email to user
$userSubject = "Application Received - SCUBE Industries";
$userMessage = "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background-color: #02204c; color: white; padding: 20px; border-radius: 5px 5px 0 0; }
        .content { background-color: #f9f9f9; padding: 20px; border: 1px solid #ddd; }
        .footer { background-color: #f0f0f0; padding: 15px; text-align: center; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>Thank you for applying to SCUBE Industries</h2>
        </div>
        <div class='content'>
            <p>Dear " . htmlspecialchars($fullName) . ",</p>
            <p>We have received your application for the position of <strong>" . htmlspecialchars($position) . "</strong>.</p>
            <p>Our HR team will review your profile and get back to you within 5-7 business days.</p>
            <p><strong>Application Details:</strong></p>
            <p><strong>Position:</strong> " . htmlspecialchars($position) . "</p>
            <p><strong>Location:</strong> " . htmlspecialchars($location) . "</p>
            <p>Best regards,<br>SCUBE Industries HR Team</p>
        </div>
        <div class='footer'>
            <p>This is an automated response. Please do not reply to this email.</p>
        </div>
    </div>
</body>
</html>
";

// Set email headers
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type: text/html; charset=UTF-8" . "\r\n";
$headers .= "From: " . $adminEmail . "\r\n";

// Handle file attachment if resume exists
if (!empty($resumeAttachment) && file_exists($resumeAttachment)) {
    // For file attachment, we need to use a different approach
    // Read file content
    $fileContent = file_get_contents($resumeAttachment);
    $fileContent = chunk_split(base64_encode($fileContent));
    
    // Create boundary
    $boundary = md5(time());
    
    // Update headers for multipart
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type: multipart/mixed; boundary=\"" . $boundary . "\"" . "\r\n";
    $headers .= "From: " . $adminEmail . "\r\n";
    
    // Create multipart message
    $adminMessage = "--" . $boundary . "\r\n";
    $adminMessage .= "Content-Type: text/html; charset=\"UTF-8\"\r\n";
    $adminMessage .= "Content-Transfer-Encoding: 7bit\r\n\r\n";
    $adminMessage .= "
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background-color: #02204c; color: white; padding: 20px; border-radius: 5px 5px 0 0; }
        .content { background-color: #f9f9f9; padding: 20px; border: 1px solid #ddd; }
        .field { margin-bottom: 15px; }
        .label { font-weight: bold; color: #02204c; }
        .value { color: #555; margin-top: 5px; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h2>New Career Application</h2>
        </div>
        <div class='content'>
            <div class='field'>
                <div class='label'>Name:</div>
                <div class='value'>" . htmlspecialchars($fullName) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Email:</div>
                <div class='value'>" . htmlspecialchars($email) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Phone:</div>
                <div class='value'>" . htmlspecialchars($phone) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Location:</div>
                <div class='value'>" . htmlspecialchars($location) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Position Applied For:</div>
                <div class='value'>" . htmlspecialchars($position) . "</div>
            </div>
            <div class='field'>
                <div class='label'>Resume:</div>
                <div class='value'>See attached file</div>
            </div>
        </div>
    </div>
</body>
</html>
" . "\r\n\r\n";
    
    // Add attachment
    $adminMessage .= "--" . $boundary . "\r\n";
    $adminMessage .= "Content-Type: application/pdf; name=\"" . basename($resumeFileName) . "\"\r\n";
    $adminMessage .= "Content-Transfer-Encoding: base64\r\n";
    $adminMessage .= "Content-Disposition: attachment; filename=\"" . basename($resumeFileName) . "\"\r\n\r\n";
    $adminMessage .= $fileContent . "\r\n";
    $adminMessage .= "--" . $boundary . "--";
}

// Send emails
$adminEmailSent = mail($adminEmail, $adminSubject, $adminMessage, $headers);
$userEmailSent = mail($email, $userSubject, $userMessage, "MIME-Version: 1.0\r\nContent-type: text/html; charset=UTF-8\r\nFrom: " . $adminEmail);

// Clean up uploaded file after sending
if (!empty($resumeAttachment) && file_exists($resumeAttachment)) {
    unlink($resumeAttachment);
}

if ($adminEmailSent && $userEmailSent) {
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'Application submitted successfully!'
    ]);
} else {
    http_response_code(500);
    echo json_encode([
        'error' => 'Failed to submit application. Please try again later.'
    ]);
}
?>
