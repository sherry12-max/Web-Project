#!/usr/bin/env python3
"""
WeasyPrint Test Script for Creative Portfolio Resume Template
Assignment 4: Resume Template Design

This script tests the creative portfolio resume template with WeasyPrint to ensure
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
    """Test the creative portfolio resume template with WeasyPrint"""
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Paths to template files
    html_file = os.path.join(script_dir, 'sample.html')
    css_file = os.path.join(script_dir, 'style.css')
    output_file = os.path.join(script_dir, 'creative_portfolio_output.pdf')
    
    # Check if files exist
    if not os.path.exists(html_file):
        print(f"❌ Error: HTML file not found at {html_file}")
        return False
        
    if not os.path.exists(css_file):
        print(f"❌ Error: CSS file not found at {css_file}")
        return False
    
    try:
        print("🔄 Testing creative portfolio resume template with WeasyPrint...")
        
        # Create HTML document from file
        html_doc = HTML(filename=html_file)
        
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
    print("🎯 Assignment 4: Creative Portfolio Resume Template WeasyPrint Test")
    print("=" * 60)
    
    success = test_resume_template()
    
    if success:
        print("\n✅ Creative Portfolio template is WeasyPrint compatible!")
        print("📋 Next steps:")
        print("   1. Open creative_portfolio_output.pdf to review the generated PDF")
        print("   2. Check that all styling is preserved")
        print("   3. Verify A4 page format and print-friendly layout")
        print("   4. Confirm creative design elements are intact")
    else:
        print("\n❌ Template needs fixes for WeasyPrint compatibility")
        sys.exit(1)

if __name__ == "__main__":
    main()
