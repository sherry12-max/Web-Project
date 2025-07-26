# Creative Portfolio Resume Template - Assignment 4

## 📋 Overview

This is a vibrant, creative resume template designed for the Web Technologies course assignment. The template features a bold, artistic design optimized for both web viewing and PDF generation using WeasyPrint, perfect for creative professionals.

**Student Information:**
- **Roll Number**: f2023266322
- **Course**: Web Technologies
- **Instructor**: Muhammad Usman Sarwar
- **Assignment**: Resume Template Design

## 🎨 Design Inspiration & Notes (100-150 words)

My creative portfolio resume template draws inspiration from modern art galleries and contemporary design studios, emphasizing bold colors and dynamic layouts. The design features a striking orange gradient (#ff6b35 to #f7931e) that creates energy and creativity while maintaining professional appeal. I chose the Montserrat font family for its modern geometric characteristics and strong visual presence.

Unique elements include an asymmetric two-column layout with creative section dividers, vibrant color blocks for visual interest, and artistic typography treatments. The template incorporates CSS Grid and Flexbox for responsive behavior while ensuring perfect A4 print compatibility through WeasyPrint. Portfolio sections use card-based layouts, and skills are represented through creative visual indicators. The design philosophy balances artistic expression with professional functionality, creating an eye-catching yet readable resume perfect for designers, artists, marketers, and other creative professionals seeking to showcase their personality.

## 🔧 Technical Features

### Fonts & Typography
- **Primary Font**: Montserrat (Google Fonts) - Modern geometric sans-serif
- **Fallback Fonts**: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto)
- **Font Weights**: 300, 400, 500, 600, 700, 800 for strong typographic hierarchy

### Color Palette
- **Primary**: #ff6b35 (Vibrant Orange)
- **Secondary**: #f7931e (Golden Orange)
- **Accent**: #4ecdc4 (Turquoise)
- **Text**: #2c3e50 (Dark Blue-Gray)
- **Background**: #ffffff (Pure White)

### Unique Design Elements
1. **Bold Color Scheme**: Eye-catching orange and turquoise combination
2. **Asymmetric Layout**: Creative two-column design with dynamic spacing
3. **Artistic Sections**: Creative dividers and visual elements
4. **Card-based Design**: Portfolio items in attractive cards
5. **Print Optimization**: Specific styles for A4 PDF generation

## 📱 Responsive Design

The template adapts to different screen sizes:
- **Desktop**: Two-column asymmetric layout with full creative elements
- **Tablet**: Maintained layout with adjusted spacing and sizing
- **Mobile**: Single-column stack with optimized creative elements

## 🖨️ Print & PDF Compatibility

Optimized for WeasyPrint with:
- A4 page size (210 × 297 mm)
- Proper page margins (0.5 inch)
- Print-safe colors and fonts
- Page break controls
- Exact color reproduction

## 📁 File Structure

```
f2023266322/
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
HTML("resume_templates/f2023266322/sample.html").write_pdf("creative_resume.pdf")
```

## 🎯 Template Sections

1. **Header Section**
   - Name with artistic typography
   - Professional title with creative styling
   - Contact information with colorful icons

2. **Left Column (Main Content)**
   - Professional Experience with creative formatting
   - Portfolio/Projects with card-based layout

3. **Right Column (Sidebar)**
   - About/Summary with artistic background
   - Skills with creative indicators
   - Education with colorful accents
   - Certifications and achievements

## 🔧 Customization

### Changing Colors
Modify the CSS variables in `style.css`:
```css
/* Update color scheme */
:root {
    --primary-color: #your-primary-color;
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
- [x] Creative, professional appearance
- [x] Proper typographic hierarchy

## 🎓 Academic Compliance

This template is completely original and designed specifically for this assignment. No existing templates were copied or modified. All design decisions were made to create a unique, creative resume layout suitable for modern creative professionals.

---

**Created for**: Web Technologies Course - Assignment 4  
**Student Roll Number**: f2023266322  
**Instructor**: Muhammad Usman Sarwar  
**Date**: July 2025
