import nodemailer from 'nodemailer';
import formidable from 'formidable';
import fs from 'fs';
import path from 'path';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const form = formidable({ multiples: false });
    const [fields, files] = await form.parse(req);

    const fullName = fields.fullName?.[0];
    const email = fields.email?.[0];
    const phone = fields.phone?.[0];
    const location = fields.location?.[0];
    const position = fields.position?.[0];
    const resume = files.resume?.[0];

    // Validate required fields
    if (!fullName || !email || !phone || !location || !position) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Create transporter using Gmail
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_PASSWORD,
      },
    });

    // Prepare attachments
    const attachments = [];
    if (resume) {
      const fileContent = fs.readFileSync(resume.filepath);
      attachments.push({
        filename: resume.originalFilename,
        content: fileContent,
      });
    }

    // Email to admin
    const adminMailOptions = {
      from: process.env.GMAIL_USER,
      to: 'sales@scubeindustries.com',
      subject: `New Career Application: ${position}`,
      html: `
        <h2>New Career Application</h2>
        <p><strong>Name:</strong> ${fullName}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Phone:</strong> ${phone}</p>
        <p><strong>Location:</strong> ${location}</p>
        <p><strong>Position Applied For:</strong> ${position}</p>
        <p><strong>Resume:</strong> See attached file</p>
      `,
      attachments: attachments,
    };

    // Auto-reply email to user
    const userMailOptions = {
      from: process.env.GMAIL_USER,
      to: email,
      subject: 'Application Received - SCUBE Industries',
      html: `
        <h2>Thank you for applying to SCUBE Industries</h2>
        <p>Dear ${fullName},</p>
        <p>We have received your application for the position of <strong>${position}</strong>.</p>
        <p>Our HR team will review your profile and get back to you within 5-7 business days.</p>
        <p><strong>Application Details:</strong></p>
        <p><strong>Position:</strong> ${position}</p>
        <p><strong>Location:</strong> ${location}</p>
        <p>Best regards,<br>SCUBE Industries HR Team</p>
      `,
    };

    // Send both emails
    await transporter.sendMail(adminMailOptions);
    await transporter.sendMail(userMailOptions);

    return res.status(200).json({ 
      success: true, 
      message: 'Application submitted successfully!' 
    });
  } catch (error) {
    console.error('Application error:', error);
    return res.status(500).json({ 
      error: 'Failed to submit application. Please try again later.' 
    });
  }
}
