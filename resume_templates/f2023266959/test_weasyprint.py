#!/usr/bin/env python3
"""
WeasyPrint Test Script for Resume Template
Assignment 4: Resume Template Design

This script tests the resume template with WeasyPrint to ensure
it renders correctly as a PDF.

Usage:
    python test_weasyprint.py

Requirements:
    pip install weasyprint
"""

from weasyprint import HTML, CSS
import os
import sys

def test_resume_template():
    """Test the resume template with WeasyPrint"""
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Paths to template files
    html_file = os.path.join(script_dir, 'index.html')
    css_file = os.path.join(script_dir, 'style.css')
    output_file = os.path.join(script_dir, 'output_resume.pdf')
    
    # Check if files exist
    if not os.path.exists(html_file):
        print(f"❌ Error: HTML file not found at {html_file}")
        return False
        
    if not os.path.exists(css_file):
        print(f"❌ Error: CSS file not found at {css_file}")
        return False
    
    try:
        print("🔄 Testing resume template with WeasyPrint...")
        
        # Read HTML content
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Create sample data for testing (replace Django template variables)
        sample_data = {
            '{{ resume.user.get_full_name|default:resume.user.username }}': 'John Doe',
            '{{ resume.title|default:"Professional" }}': 'Software Engineer',
            '{{ resume.summary|default:"Professional summary will appear here." }}': 'Experienced software engineer with 5+ years of expertise in full-stack development, specializing in Python, JavaScript, and cloud technologies.',
            '{{ resume.user.email }}': 'john.doe@email.com',
            '{{ resume.user.profile.phone }}': '+1 (555) 123-4567',
            '{{ resume.user.profile.location }}': 'San Francisco, CA',
            '{{ resume.user.profile.linkedin }}': 'linkedin.com/in/johndoe',
        }
        
        # Replace Django template variables with sample data
        for template_var, sample_value in sample_data.items():
            html_content = html_content.replace(template_var, sample_value)
        
        # Remove Django template tags for testing
        import re
        html_content = re.sub(r'{%.*?%}', '', html_content)
        html_content = re.sub(r'{{.*?}}', 'Sample Data', html_content)
        
        # Create HTML document
        html_doc = HTML(string=html_content, base_url=f'file://{script_dir}/')
        
        # Generate PDF
        print("📄 Generating PDF...")
        html_doc.write_pdf(output_file)
        
        print(f"✅ Success! PDF generated at: {output_file}")
        print(f"📊 File size: {os.path.getsize(output_file)} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("🎯 Assignment 4: Resume Template WeasyPrint Test")
    print("=" * 60)
    
    success = test_resume_template()
    
    if success:
        print("\n✅ Template is WeasyPrint compatible!")
        print("📋 Next steps:")
        print("   1. Open output_resume.pdf to review the generated PDF")
        print("   2. Check that all styling is preserved")
        print("   3. Verify A4 page format and print-friendly layout")
    else:
        print("\n❌ Template needs fixes for WeasyPrint compatibility")
        sys.exit(1)

if __name__ == "__main__":
    main()
