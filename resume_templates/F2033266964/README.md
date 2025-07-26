# Corporate Executive Resume Template - Assignment 4

## 📋 Overview

This is an elegant, executive-level resume template designed for the Web Technologies course assignment. The template features a sophisticated, corporate design optimized for both web viewing and PDF generation using WeasyPrint, perfect for senior professionals and executives.

**Student Information:**
- **Roll Number**: f2023266323
- **Course**: Web Technologies
- **Instructor**: Muhammad Usman Sarwar
- **Assignment**: Resume Template Design

## 🎨 Design Inspiration & Notes (100-150 words)

My corporate executive resume template draws inspiration from luxury business publications and high-end corporate branding, emphasizing sophistication and authority. The design features an elegant navy blue color scheme (#1e3a8a to #3730a3) that conveys trust, professionalism, and executive presence. I chose the Playfair Display font for headings to add elegance, paired with Source Sans Pro for body text to ensure readability.

Unique elements include a distinguished header with executive-style typography, premium section dividers with subtle shadows, and a refined three-column layout that maximizes content while maintaining elegance. The template incorporates advanced CSS techniques for sophisticated visual effects while ensuring perfect A4 print compatibility through WeasyPrint. Achievement metrics are highlighted prominently, and the overall design philosophy focuses on conveying leadership, experience, and corporate excellence. This template is ideal for C-level executives, senior managers, and established professionals seeking to project authority and competence.

## 🔧 Technical Features

### Fonts & Typography
- **Primary Font**: Playfair Display (Google Fonts) - Elegant serif for headings
- **Secondary Font**: Source Sans Pro (Google Fonts) - Professional sans-serif for body
- **Fallback Fonts**: System fonts (Georgia, Times, serif for headings; Arial, sans-serif for body)
- **Font Weights**: 300, 400, 500, 600, 700, 900 for sophisticated hierarchy

### Color Palette
- **Primary**: #1e3a8a (Navy Blue)
- **Secondary**: #3730a3 (Royal Purple)
- **Accent**: #dc2626 (Executive Red)
- **Text**: #1f2937 (Charcoal)
- **Background**: #f8fafc (Light Gray)

### Unique Design Elements
1. **Executive Header**: Distinguished typography with professional styling
2. **Three-Column Layout**: Sophisticated content organization
3. **Premium Shadows**: Subtle depth and elegance
4. **Achievement Highlights**: Prominent metrics and accomplishments
5. **Print Optimization**: Executive-quality PDF output

## 📱 Responsive Design

The template adapts to different screen sizes:
- **Desktop**: Three-column executive layout with full sophistication
- **Tablet**: Two-column layout maintaining elegance
- **Mobile**: Single-column stack with preserved executive styling

## 🖨️ Print & PDF Compatibility

Optimized for WeasyPrint with:
- A4 page size (210 × 297 mm)
- Executive margins (0.75 inch)
- Print-safe colors and fonts
- Page break controls
- Professional color reproduction

## 📁 File Structure

```
f2023266323/
├── index.html          # Main HTML template
├── style.css          # Complete CSS styling
├── sample.html        # Standalone version
├── README.md          # This documentation
└── test_weasyprint.py # WeasyPrint test script
```

## 🚀 How to Use

### Preview in Browser
1. Open `sample.html` in any modern web browser
2. The template will display with sample data
3. Responsive design can be tested by resizing the browser window

### Generate PDF with WeasyPrint

#### Installation
```bash
pip install weasyprint
```

#### Basic Usage
```python
from weasyprint import HTML

# Generate PDF from HTML file
HTML("resume_templates/f2023266323/sample.html").write_pdf("executive_resume.pdf")
```

## 🎯 Template Sections

1. **Executive Header**
   - Name with distinguished typography
   - Executive title and credentials
   - Professional contact information

2. **Left Column (Primary)**
   - Executive Summary with key achievements
   - Professional Experience with metrics
   - Leadership accomplishments

3. **Center Column (Secondary)**
   - Core competencies and skills
   - Education and certifications
   - Professional affiliations

4. **Right Column (Tertiary)**
   - Key achievements and awards
   - Board positions and directorships
   - Languages and additional qualifications

## 🔧 Customization

### Changing Colors
Modify the CSS variables in `style.css`:
```css
/* Update executive color scheme */
:root {
    --primary-color: #your-executive-color;
    --secondary-color: #your-secondary-color;
    --accent-color: #your-accent-color;
}
```

## ✅ Validation Checklist

- [x] A4 page size compatibility
- [x] WeasyPrint PDF generation tested
- [x] Responsive design implemented
- [x] Semantic HTML5 elements used
- [x] Print-safe colors and fonts
- [x] No JavaScript dependencies
- [x] Executive, sophisticated appearance
- [x] Proper typographic hierarchy

## 🎓 Academic Compliance

This template is completely original and designed specifically for this assignment. No existing templates were copied or modified. All design decisions were made to create a unique, executive-level resume layout suitable for senior professionals and corporate leaders.

---

**Created for**: Web Technologies Course - Assignment 4  
**Student Roll Number**: f2023266323  
**Instructor**: Muhammad Usman Sarwar  
**Date**: July 2025
