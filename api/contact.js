import nodemailer from 'nodemailer';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { firstName, lastName, email, phone, subject, message } = req.body;

  // Validate required fields
  if (!firstName || !lastName || !email || !phone || !subject || !message) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  try {
    // Create transporter using Gmail
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: process.env.GMAIL_USER,
        pass: process.env.GMAIL_PASSWORD,
      },
    });

    // Email to admin
    const adminMailOptions = {
      from: process.env.GMAIL_USER,
      to: 'sales@scubeindustries.com',
      subject: `New Contact Form Submission: ${subject}`,
      html: `
        <h2>New Contact Form Submission</h2>
        <p><strong>Name:</strong> ${firstName} ${lastName}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Phone:</strong> ${phone}</p>
        <p><strong>Subject:</strong> ${subject}</p>
        <p><strong>Message:</strong></p>
        <p>${message.replace(/\n/g, '<br>')}</p>
      `,
    };

    // Auto-reply email to user
    const userMailOptions = {
      from: process.env.GMAIL_USER,
      to: email,
      subject: 'We received your message - SCUBE Industries',
      html: `
        <h2>Thank you for contacting SCUBE Industries</h2>
        <p>Dear ${firstName},</p>
        <p>We have received your message and will get back to you as soon as possible.</p>
        <p><strong>Your Message Details:</strong></p>
        <p><strong>Subject:</strong> ${subject}</p>
        <p><strong>Message:</strong></p>
        <p>${message.replace(/\n/g, '<br>')}</p>
        <p>Best regards,<br>SCUBE Industries Team</p>
      `,
    };

    // Send both emails
    await transporter.sendMail(adminMailOptions);
    await transporter.sendMail(userMailOptions);

    return res.status(200).json({ 
      success: true, 
      message: 'Message sent successfully!' 
    });
  } catch (error) {
    console.error('Email error:', error);
    return res.status(500).json({ 
      error: 'Failed to send message. Please try again later.' 
    });
  }
}
