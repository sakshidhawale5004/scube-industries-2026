# GitHub Deployment Guide for SCUBE Industries Website

## Step 1: Create GitHub Repository

1. Go to **https://github.com/new**
2. Enter Repository name: `scubeindustries` (or your preferred name)
3. Choose **Public** (so GitHub Pages works)
4. ✅ Check "Add a README file"
5. Click **Create repository**

---

## Step 2: Prepare Your Local Project

### Clone the repository to your computer:
```bash
cd C:\Users\Sakshi\Downloads
git clone https://github.com/YOUR_USERNAME/scubeindustries.git
cd scubeindustries
```

### Copy your website files:
- Copy all files from `scube1/scube1/` folder into the `scubeindustries` folder
- Include: index.html, aboutus.html, products.html, all other .html files, and logo.png.jpeg

### Final structure should be:
```
scubeindustries/
├── index.html
├── aboutus.html
├── products.html
├── contact.html
├── services.html
├── careers.html
├── news.html
├── logo.png.jpeg
├── css/
├── js/
├── fonts/
├── README.md
└── .gitignore
```

---

## Step 3: Initialize & Push to GitHub

Open PowerShell in the `scubeindustries` folder and run:

```powershell
# Check git status
git status

# Stage all files
git add .

# Commit files
git commit -m "Initial commit: SCUBE Industries website"

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top-right menu)
3. Scroll down to **Pages** section (left sidebar)
4. Under "Build and deployment":
   - Source: Select **Deploy from a branch**
   - Branch: Select **main** and **/root**
5. Click **Save**
6. Wait 1-2 minutes for deployment

---

## Step 5: Your Website is Live! 🎉

Your site will be available at:
```
https://YOUR_USERNAME.github.io/scubeindustries
```

**Example:** If your username is `sakshi123`, your website URL will be:
```
https://sakshi123.github.io/scubeindustries
```

---

## Important Notes:

- **Custom Domain?** You can add a custom domain in GitHub Pages settings if you have one
- **Updates:** After making changes, just commit and push again:
  ```
  git add .
  git commit -m "Updated content"
  git push
  ```
- **Build time:** GitHub Pages takes 1-2 minutes to deploy changes

---

## Troubleshooting:

**If pages don't appear:**
- Wait 2-3 minutes (GitHub Pages might be building)
- Check Settings → Pages to confirm deployment is enabled
- Verify index.html is in the root folder

**If files won't push:**
- Make sure you have Git installed: `git --version`
- Check your GitHub credentials are set up

---

## Optional: Add .gitignore

Create a `.gitignore` file in your root folder with:
```
.DS_Store
Thumbs.db
*.bak
node_modules/
```

This prevents unnecessary files from being uploaded.
