# Vercel Functions Setup Guide - Form Backend

## Overview
Your contact and careers forms now use **Vercel Functions** - a serverless backend that runs on Vercel with email notifications.

## Features
✅ **Unlimited Submissions** - No limits
✅ **Email Notifications** - Automatic emails to admin and user
✅ **File Uploads** - Resume uploads supported
✅ **Auto-replies** - Users get confirmation emails
✅ **No External Services** - Everything on Vercel
✅ **Secure** - Backend validation and error handling

## Setup Steps

### Step 1: Set Up Gmail App Password
1. Go to https://myaccount.google.com/
2. Click **Security** (left sidebar)
3. Enable **2-Step Verification** (if not already enabled)
4. Go back to Security
5. Find **App passwords** (appears after 2FA is enabled)
6. Select **Mail** and **Windows Computer** (or your device)
7. Google will generate a 16-character password
8. Copy this password (you'll need it in Step 2)

### Step 2: Add Environment Variables to Vercel
1. Go to https://vercel.com/dashboard
2. Select your **scube-industry** project
3. Click **Settings** → **Environment Variables**
4. Add two new variables:
   - **Name:** `GMAIL_USER`
   - **Value:** `sales@scubeindustries.com`
   
5. Add another variable:
   - **Name:** `GMAIL_PASSWORD`
   - **Value:** (paste the 16-character password from Step 1)

6. Click **Save**

### Step 3: Deploy to Vercel
1. Push your code to GitHub:
   ```bash
   git add -A
   git commit -m "Add Vercel Functions for form backend"
   git push origin main
   ```

2. Vercel will automatically detect changes and redeploy
3. Wait for deployment to complete (check Vercel dashboard)

### Step 4: Test the Forms
1. Go to https://scube-industry.vercel.app/contact.html
2. Fill out the contact form and submit
3. Check your email (sales@scubeindustries.com) for the submission
4. Check your personal email for the auto-reply

## How It Works

### Contact Form Flow:
1. User fills form on website
2. JavaScript sends data to `/api/contact`
3. Vercel Function receives request
4. Email sent to admin (sales@scubeindustries.com)
5. Auto-reply sent to user
6. Success message shown to user

### Careers Form Flow:
1. User fills form and uploads resume
2. JavaScript sends data to `/api/careers`
3. Vercel Function receives request
4. Resume attached to email
5. Email sent to admin with resume
6. Auto-reply sent to user
7. Success message shown to user

## API Endpoints

### Contact Form
- **Endpoint:** `/api/contact`
- **Method:** POST
- **Fields:** firstName, lastName, email, phone, subject, message

### Careers Form
- **Endpoint:** `/api/careers`
- **Method:** POST
- **Fields:** fullName, email, phone, location, position, resume (file)

## Troubleshooting

### Forms not submitting?
1. Check browser console (F12) for errors
2. Verify environment variables are set in Vercel
3. Check Vercel deployment logs

### Not receiving emails?
1. Verify Gmail app password is correct
2. Check spam/junk folder
3. Verify email address in environment variables
4. Check Vercel function logs for errors

### Resume not attached?
1. Ensure file is PDF format
2. Check file size (should be < 25MB)
3. Verify formidable package is installed

## Environment Variables Reference

```
GMAIL_USER=sales@scubeindustries.com
GMAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

## Files Created/Modified

### New Files:
- `/api/contact.js` - Contact form handler
- `/api/careers.js` - Careers form handler
- `package.json` - Dependencies
- `vercel.json` - Vercel configuration

### Modified Files:
- `contact.html` - Updated form to use API
- `careers.html` - Updated form to use API
- `scube1/contact.html` - Updated form to use API
- `scube1/careers.html` - Updated form to use API

## Dependencies

The following packages are used:
- **nodemailer** - Email sending
- **formidable** - File upload handling

These are automatically installed by Vercel.

## Security Notes

- Environment variables are secure and not exposed in code
- Passwords are never logged or displayed
- Form data is validated on backend
- File uploads are checked for safety

## Support

For issues:
1. Check Vercel dashboard for deployment errors
2. Review function logs in Vercel
3. Verify environment variables are set correctly
4. Check Gmail app password is valid

## Next Steps

1. Set up Gmail app password (Step 1)
2. Add environment variables to Vercel (Step 2)
3. Deploy to Vercel (Step 3)
4. Test the forms (Step 4)

---

**Status**: ✅ Ready to deploy
**Last Updated**: April 2026
