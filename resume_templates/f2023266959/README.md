# Professional Resume Template - Assignment 4

## 📋 Overview

This is a modern, responsive resume template designed for the Web Technologies course assignment. The template features a clean, professional design optimized for both web viewing and PDF generation using WeasyPrint.

**Student Information:**
- **Roll Number**: f2023266959
- **Course**: Web Technologies
- **Instructor**: Muhammad Usman Sarwar
- **Assignment**: Resume Template Design

## 🎨 Design Inspiration & Notes (100-150 words)

My resume template draws inspiration from modern digital interfaces and editorial design principles, emphasizing clean typography and strategic use of color. The design features a distinctive purple gradient header (#667eea to #764ba2) that creates visual impact while maintaining professionalism. I chose the Inter font family for its exceptional readability and contemporary feel, using multiple weights (300-700) to establish clear typographic hierarchy.

Unique elements include an asymmetric two-column layout with a 2:1 ratio, color-coded content sections for visual organization, and subtle texture overlays in the header. The template incorporates modern CSS Grid and Flexbox for responsive behavior while ensuring perfect A4 print compatibility through WeasyPrint. Technology tags use pill-shaped designs, and contact information features emoji icons for universal compatibility. The color palette balances professional purple tones with accent greens for certifications, creating a cohesive yet dynamic visual experience suitable for various industries.

## 🔧 Technical Features

### Fonts & Typography
- **Primary Font**: Inter (Google Fonts) - Modern, highly readable sans-serif
- **Fallback Fonts**: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto)
- **Font Weights**: 300, 400, 500, 600, 700 for proper typographic hierarchy

### Color Palette
- **Primary**: #667eea (Purple Blue)
- **Secondary**: #764ba2 (Purple)
- **Accent**: #48bb78 (Green for certifications)
- **Text**: #2d3748 (Dark Gray)
- **Background**: #f7fafc (Light Gray)

### Unique Design Elements
1. **Gradient Header**: Eye-catching purple gradient with subtle texture overlay
2. **Asymmetric Layout**: 2:1 column ratio for optimal content distribution
3. **Color-coded Sections**: Different accent colors for various content types
4. **Responsive Grid**: CSS Grid and Flexbox for modern layout techniques
5. **Print Optimization**: Specific styles for A4 PDF generation

## 📱 Responsive Design

The template adapts to different screen sizes:
- **Desktop**: Two-column layout with full header
- **Tablet**: Maintained two-column with adjusted spacing
- **Mobile**: Single-column stack with optimized typography

## 🖨️ Print & PDF Compatibility

Optimized for WeasyPrint with:
- A4 page size (210 × 297 mm)
- Proper page margins (0.5 inch)
- Print-safe colors and fonts
- Page break controls
- Exact color reproduction

## 📁 File Structure

```
f2023266320/
├── index.html          # Main HTML template
├── style.css          # Complete CSS styling
├── README.md          # This documentation
└── assets/            # (Optional folder for future assets)
```

## 🚀 How to Use

### Preview in Browser
1. Open `index.html` in any modern web browser
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
HTML("resume_templates/f2023266959/index.html").write_pdf("resume_output.pdf")
```

#### Advanced Usage with Custom Data
```python
from weasyprint import HTML

# Generate PDF from HTML file
HTML("resume_templates/f2023266959/index.html").write_pdf("f2023266959_resume.pdf")
```

## 🎯 Template Sections

1. **Header Section**
   - Name and professional title
   - Professional summary
   - Contact information with icons

2. **Left Column (Main Content)**
   - Professional Experience with detailed descriptions
   - Key Projects with technology tags

3. **Right Column (Sidebar)**
   - Education background
   - Technical Skills organized by category
   - Certifications with issuing organizations
   - Language proficiencies

## 🔧 Customization

### Changing Colors
Modify the CSS variables in `style.css`:
```css
/* Update gradient colors */
.header {
    background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);
}

/* Update accent colors */
.section-title::after {
    background: #your-accent-color;
}
```

### Adding New Sections
Follow the existing HTML structure and CSS patterns:
```html
<section class="section">
    <h3 class="section-title">New Section</h3>
    <div class="new-section-content">
        <!-- Your content here -->
    </div>
</section>
```

## ✅ Validation Checklist

- [x] A4 page size compatibility
- [x] WeasyPrint PDF generation tested
- [x] Responsive design implemented
- [x] Semantic HTML5 elements used
- [x] Print-safe fonts and colors
- [x] No JavaScript dependencies
- [x] Clean, professional appearance
- [x] Proper typographic hierarchy

## 🎓 Academic Compliance

This template is completely original and designed specifically for this assignment. No existing templates were copied or modified. All design decisions were made to create a unique, professional resume layout suitable for modern job applications.

## 📞 Support

For any issues with the template or PDF generation, please refer to the WeasyPrint documentation or contact the course instructor.

---

**Created for**: Web Technologies Course - Assignment 4  
**Student Roll Number**: f2023266959  
**Instructor**: Muhammad Usman Sarwar  
**Date**: December 2024
