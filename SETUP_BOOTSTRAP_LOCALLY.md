# Setting Up Bootstrap 5 Locally

Follow these steps to download and set up all dependencies locally:

## 1. Bootstrap 5 CSS and JS

Download Bootstrap 5.3.0:
- Go to: https://getbootstrap.com/docs/5.3/getting-started/download/
- Click "Download" to get bootstrap-5.3.0-dist.zip
- Extract the ZIP file
- Copy `bootstrap.min.css` from the extracted folder to: `css/`
- Copy `bootstrap.bundle.min.js` from the extracted folder to: `js/`

## 2. Font Awesome Icons

Download Font Awesome 6.4.0:
- Go to: https://fontawesome.com/download
- Download the free version
- Extract the ZIP file
- Copy the entire `webfonts` folder to: `fonts/`
- Copy `css/all.min.css` to: `css/`

## 3. Google Fonts (Montserrat)

Option A - Download Font Files:
- Go to: https://fonts.google.com/specimen/Montserrat
- Click "Download family"
- Extract and copy font files to: `fonts/`
- Use the provided CSS to reference them locally

Option B - Keep CDN (Simpler):
- The current setup already uses Google Fonts CDN which works offline cached if previously loaded
- You can keep the Google Fonts CDN link as-is

## Folder Structure After Setup

```
scube1/
  ├── index.html
  ├── css/
  │   ├── bootstrap.min.css
  │   └── all.min.css (Font Awesome)
  ├── js/
  │   └── bootstrap.bundle.min.js
  ├── fonts/
  │   └── webfonts/ (Font Awesome fonts)
  │   └── [Montserrat font files] (optional)
  └── ... (other HTML files)
```

## Files Ready to Download in This Project

The `index.html` file has already been updated to reference all these local files. 
Just place the downloaded files in the directories as specified above.

## Testing

Once files are in place, open `index.html` in your browser without internet and it should work completely offline.
