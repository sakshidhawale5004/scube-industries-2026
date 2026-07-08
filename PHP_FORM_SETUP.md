# PHP Form Backend Setup Guide - Hostinger

## Overview
Your contact and careers forms now use **PHP backend** running on Hostinger with automatic email notifications.

## Features
✅ **Unlimited Submissions** - No limits
✅ **Email Notifications** - Automatic emails to admin and user
✅ **File Uploads** - Resume uploads with email attachment
✅ **Auto-replies** - Users get confirmation emails
✅ **Form Validation** - Server-side validation
✅ **Security** - Input sanitization and validation

## Files Created

### Backend Files:
- `/api/contact.php` - Contact form handler
- `/api/careers.php` - Careers form handler

### Updated Files:
- `contact.html` - Updated form to use PHP API
- `careers.html` - Updated form to use PHP API
- `scube1/contact.html` - Updated form to use PHP API
- `scube1/careers.html` - Updated form to use PHP API

## How It Works

### Contact Form Flow:
1. User fills form on website
2. JavaScript sends data to `api/contact.php`
3. PHP validates the data
4. Email sent to admin (sales@scubeindustries.com)
5. Auto-reply sent to user
6. Success message shown to user

### Careers Form Flow:
1. User fills form and uploads resume
2. JavaScript sends data to `api/careers.php`
3. PHP validates the data and file
4. Resume attached to email
5. Email sent to admin with resume
6. Auto-reply sent to user
7. Success message shown to user

## Setup Steps

### Step 1: Upload Files to Hostinger
1. Go to Hostinger File Manager
2. Navigate to your website root directory (usually `public_html`)
3. Create a folder named `api` (if it doesn't exist)
4. Upload these files to the `api` folder:
   - `contact.php`
   - `careers.php`

### Step 2: Set Permissions
1. Right-click on `api` folder
2. Click **Permissions**
3. Set to **755** (read, write, execute for owner; read and execute for others)
4. Apply to all files inside

### Step 3: Create Uploads Directory (for resumes)
1. In the `api` folder, create a new folder named `uploads`
2. Inside `uploads`, create a folder named `resumes`
3. Set permissions to **755**

### Step 4: Test the Forms
1. Go to your website contact page
2. Fill out the contact form and submit
3. Check your email (sales@scubeindustries.com) for the submission
4. Check your personal email for the auto-reply

## API Endpoints

### Contact Form
- **Endpoint:** `api/contact.php`
- **Method:** POST
- **Fields:** firstName, lastName, email, phone, subject, message

### Careers Form
- **Endpoint:** `api/careers.php`
- **Method:** POST
- **Fields:** fullName, email, phone, location, position, resume (file)

## Email Configuration

The PHP scripts use Hostinger's built-in mail function. No additional configuration needed!

### Admin Email:
- Receives: Contact submissions and career applications
- Email: sales@scubeindustries.com

### User Email:
- Receives: Auto-reply confirmation
- Email: User's email address from form

## Troubleshooting

### Forms not submitting?
1. Check browser console (F12) for errors
2. Verify `api` folder exists and has correct permissions
3. Check Hostinger error logs

### Not receiving emails?
1. Check spam/junk folder
2. Verify email address in form
3. Check Hostinger mail settings
4. Verify PHP mail function is enabled

### Resume not attaching?
1. Ensure `api/uploads/resumes` folder exists
2. Check folder permissions (should be 755)
3. Verify file is PDF format
4. Check file size (should be < 5MB)

### Permission Denied Error?
1. Right-click folder → Permissions
2. Set to 755
3. Check "Apply to all files inside"

## File Structure

```
public_html/
├── index.html
├── contact.html
├── careers.html
├── api/
│   ├── contact.php
│   ├── careers.php
│   └── uploads/
│       └── resumes/
│           └── (uploaded resume files)
└── ... (other files)
```

## Security Features

✅ **Input Validation** - All fields validated
✅ **Email Validation** - Email format checked
✅ **File Validation** - Only PDF files allowed
✅ **File Size Limit** - Max 5MB per file
✅ **HTML Escaping** - Prevents XSS attacks
✅ **Error Handling** - Graceful error messages

## Email Templates

### Contact Form Email (to admin):
- Sender: sales@scubeindustries.com
- Subject: "New Contact Form Submission: [Subject]"
- Contains: Name, Email, Phone, Subject, Message

### Careers Form Email (to admin):
- Sender: sales@scubeindustries.com
- Subject: "New Career Application: [Position]"
- Contains: Name, Email, Phone, Location, Position, Resume (attached)

### Auto-reply (to user):
- Sender: sales@scubeindustries.com
- Subject: "We received your message - SCUBE Industries"
- Contains: Confirmation message and submission details

## Hostinger Specific Notes

### Mail Function:
- Hostinger supports PHP mail() function
- No SMTP configuration needed
- Emails sent from your hosting account

### File Uploads:
- Max upload size: Check Hostinger settings (usually 128MB)
- Temp directory: Automatically handled by Hostinger
- Storage: Included in your hosting plan

### PHP Version:
- Works with PHP 7.4+
- Recommended: PHP 8.0+
- Check your Hostinger panel for current version

## Support

For issues:
1. Check Hostinger error logs (cPanel → Error Log)
2. Verify file permissions
3. Test with simple form first
4. Check email spam folder

## Next Steps

1. Upload `api/contact.php` and `api/careers.php` to Hostinger
2. Create `api/uploads/resumes` folder
3. Set permissions to 755
4. Test the forms
5. Check emails

---

**Status**: ✅ Ready to deploy
**Last Updated**: April 2026
**Platform**: Hostinger
