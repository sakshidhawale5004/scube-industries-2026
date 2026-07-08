# Form Setup Instructions - Basin Integration (Unlimited & Free)

## Overview
The contact and careers forms have been updated to use **Basin**, a completely free form backend service that handles unlimited form submissions without requiring any verification or backend code.

## Why Basin?
✅ **Completely Free** - No monthly limits or costs
✅ **Unlimited Submissions** - Send as many as you want
✅ **No Verification Needed** - Just create and use
✅ **No Backend Required** - Works on static hosting (Vercel)
✅ **File Uploads** - Support for resume uploads (up to 10GB storage)
✅ **Spam Protection** - Built-in spam filtering
✅ **Email Delivery** - Reliable email notifications

## Forms Updated
1. **Contact Form** (`contact.html` & `scube1/contact.html`)
   - Fields: First Name, Last Name, Email, Phone, Subject, Message
   - Sends to: sales@scubeindustries.com

2. **Careers Form** (`careers.html` & `scube1/careers.html`)
   - Fields: Full Name, Email, Phone, Location, Position, Resume
   - Sends to: sales@scubeindustries.com

## Setup Steps (Super Simple!)

### Step 1: Go to Basin
1. Visit https://usebasin.com/
2. Click **"Get Started"** or **"Create Form"**
3. No signup needed - just create your forms!

### Step 2: Create Contact Form
1. Click **"Create New Form"**
2. Name it: `Contact Form`
3. Set email to: `sales@scubeindustries.com`
4. Copy the form endpoint (looks like: `https://usebasin.com/f/abc123def456`)
5. Replace `CONTACT_FORM_ID` in these files with your endpoint ID:
   - `contact.html` - Line with `action="https://usebasin.com/f/CONTACT_FORM_ID"`
   - `scube1/contact.html` - Same line

### Step 3: Create Careers Form
1. Click **"Create New Form"** again
2. Name it: `Careers Form`
3. Set email to: `sales@scubeindustries.com`
4. Copy the form endpoint
5. Replace `CAREERS_FORM_ID` in these files with your endpoint ID:
   - `careers.html` - Line with `action="https://usebasin.com/f/CAREERS_FORM_ID"`
   - `scube1/careers.html` - Same line

### Step 4: Test the Forms
1. Go to your website
2. Fill out the contact form and submit
3. Check your email for the submission
4. Confirm it works!

## Basin Dashboard Features
- **View all submissions** - See every form submission in your inbox
- **File storage** - Up to 10GB for uploaded files
- **Spam filtering** - Automatic spam detection
- **Auto-responses** - Send confirmation emails to users
- **Integrations** - Connect to Slack, Zapier, etc.
- **Analytics** - Track form submissions

## How to Get Your Form IDs

### For Contact Form:
1. Go to https://usebasin.com/
2. Create a new form
3. The URL will be: `https://usebasin.com/f/YOUR_ID_HERE`
4. Copy just the `YOUR_ID_HERE` part
5. Replace `CONTACT_FORM_ID` in contact.html with this ID

### For Careers Form:
1. Create another form
2. Copy the ID from the URL
3. Replace `CAREERS_FORM_ID` in careers.html with this ID

## Example:
If Basin gives you: `https://usebasin.com/f/abc123def456`

Then in your HTML, change:
```html
<form action="https://usebasin.com/f/CONTACT_FORM_ID" method="POST">
```

To:
```html
<form action="https://usebasin.com/f/abc123def456" method="POST">
```

## Troubleshooting

### Form not submitting?
1. Check that the form action URL is correct
2. Verify the form ID matches your Basin form
3. Check browser console for errors (F12)

### Not receiving emails?
1. Check spam/junk folder
2. Verify email address in Basin form settings
3. Test with a different email address

### Need help?
- Basin Docs: https://usebasin.com/docs/
- Basin Support: https://usebasin.com/contact/

## Security Notes
- Basin handles all data securely
- No sensitive data stored on your server
- Spam filtering protects your inbox
- File uploads are virus scanned

## Pricing
- **Free Plan**: Unlimited forms, unlimited submissions, 10GB storage
- **No paid plans needed** - Free plan has everything!

## Alternative Solutions (if needed)
1. **EmailJS** - Client-side email sending (requires verification)
2. **Vercel Functions** - Serverless backend on Vercel
3. **Firebase** - Google's backend service
4. **AWS Lambda** - Amazon's serverless functions

---

**Status**: ✅ Ready to deploy
**Last Updated**: April 2026
**Next Step**: Get your Basin form IDs and update the HTML files
