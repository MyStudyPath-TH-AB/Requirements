import os
import json
import markdown2
from pathlib import Path

def parse_func_requirements():
    """Parse functional requirements folder structure and convert markdown to dict"""
    func_requirements = {}
    req_path = Path("Funktionale Anforderungen")
    
    for req_type in req_path.iterdir():
        if not req_type.is_dir():
            continue
        
        req_type_name = req_type.name
        func_requirements[req_type_name] = {}
        
        for topic in req_type.iterdir():
            if not topic.is_dir():
                continue
            
            topic_name = topic.name
            func_requirements[req_type_name][topic_name] = []
            
            for req_file in topic.rglob("*.md"):
                with open(req_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    html_content = markdown2.markdown(content)
                    
                    func_requirements[req_type_name][topic_name].append({
                        "file": req_file.name,
                        "path": str(req_file),
                        "content": html_content
                    })
    
    return func_requirements

def parse_nonfunc_requirements():
    """Parse functional requirements folder structure and convert markdown to dict"""
    nonfunc_requirements = {}
    req_path = Path("Nicht funktionale Anforderungen")
    
    for req_type in req_path.iterdir():
        if not req_type.is_dir():
            continue
        
        req_type_name = req_type.name
        nonfunc_requirements[req_type_name] = {}
        
        for topic in req_type.iterdir():
            if not topic.is_dir():
                continue
            
            topic_name = topic.name
            nonfunc_requirements[req_type_name][topic_name] = []
            
            for req_file in topic.rglob("*.md"):
                with open(req_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    html_content = markdown2.markdown(content)
                    
                    nonfunc_requirements[req_type_name][topic_name].append({
                        "file": req_file.name,
                        "path": str(req_file),
                        "content": html_content
                    })
    
    return nonfunc_requirements

def parse_stakeholders():
    """Parse stakeholder folder structure and convert markdown to dict"""
    stakeholders = {}
    stakeholder_path = Path("Stakeholder")
    
    for category in stakeholder_path.iterdir():
        if not category.is_dir():
            continue
        
        category_name = category.name
        stakeholders[category_name] = {}
        
        for subcategory in category.iterdir():
            if not subcategory.is_dir():
                continue
            
            subcategory_name = subcategory.name
            stakeholders[category_name][subcategory_name] = []
            
            for stakeholder_file in subcategory.rglob("*.md"):
                with open(stakeholder_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    html_content = markdown2.markdown(content)
                    
                    stakeholders[category_name][subcategory_name].append({
                        "file": stakeholder_file.name,
                        "path": str(stakeholder_file),
                        "content": html_content
                    })
    
    return stakeholders

def generate_func_requirements_html(func_requirements):
    """Generate HTML page for requirements"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Funktionale Anforderungen</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
            h1 { color: #0366d6; font-size: 2.5em; margin-bottom: 30px; border-bottom: 2px solid #0366d6; padding-bottom: 10px; }
            h2 { color: #24292e; font-size: 1.8em; margin-top: 30px; margin-bottom: 15px; }
            h3 { color: #586069; font-size: 1.3em; margin-top: 20px; margin-bottom: 10px; }
            .req-type { background: white; padding: 20px; margin-bottom: 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
            .req-item { background: #f6f8fa; padding: 15px; margin: 10px 0; border-left: 4px solid #0366d6; border-radius: 4px; }
            .req-item h4 { color: #0366d6; margin-bottom: 8px; }
            
            /* Custom styling for markdown content */
            .req-content { font-size: 0.95em; }
            .req-content h2 { font-size: 1.1em; color: #24292e; font-weight: 600; margin: 15px 0 8px 0; }
            .req-content h3 { font-size: 0.95em; color: #586069; font-weight: 600; margin: 12px 0 6px 0; }
            .req-content h4, .req-content h5, .req-content h6 { font-size: 0.9em; color: #666; font-weight: 600; margin: 10px 0 5px 0; }
            .req-content p { margin: 8px 0; }
            .req-content a { color: #0366d6; text-decoration: none; }
            .req-content a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Funktionale Anforderungen</h1>
    """
    
    for req_type, topics in func_requirements.items():
        html += f'<div class="req-type"><h2>{req_type.replace("_", " ").title()}</h2>'
        
        for topic, items in topics.items():
            html += f'<h3>{topic.replace("_", " ").title()}</h3>'
            
            for item in items:
                html += f"""
                <div class="req-item">
                    <h4>{item['file'].replace('.md', '')}</h4>
                    <div class="req-content">
                        {item['content']}
                    </div>
                </div>
                """
        
        html += '</div>'
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

def generate_nonfunc_requirements_html(nonfunc_requirements):
    """Generate HTML page for requirements"""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nicht funktionale Anforderungen</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
            h1 { color: #0366d6; font-size: 2.5em; margin-bottom: 30px; border-bottom: 2px solid #0366d6; padding-bottom: 10px; }
            h2 { color: #24292e; font-size: 1.8em; margin-top: 30px; margin-bottom: 15px; }
            h3 { color: #586069; font-size: 1.3em; margin-top: 20px; margin-bottom: 10px; }
            .req-type { background: white; padding: 20px; margin-bottom: 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
            .req-item { background: #f6f8fa; padding: 15px; margin: 10px 0; border-left: 4px solid #0366d6; border-radius: 4px; }
            .req-item h4 { color: #0366d6; margin-bottom: 8px; }
            
            /* Custom styling for markdown content */
            .req-content { font-size: 0.95em; }
            .req-content h2 { font-size: 1.1em; color: #24292e; font-weight: 600; margin: 15px 0 8px 0; }
            .req-content h3 { font-size: 0.95em; color: #586069; font-weight: 600; margin: 12px 0 6px 0; }
            .req-content h4, .req-content h5, .req-content h6 { font-size: 0.9em; color: #666; font-weight: 600; margin: 10px 0 5px 0; }
            .req-content p { margin: 8px 0; }
            .req-content a { color: #0366d6; text-decoration: none; }
            .req-content a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Nicht funktionale Anforderungen</h1>
    """
    
    for req_type, topics in nonfunc_requirements.items():
        html += f'<div class="req-type"><h2>{req_type.replace("_", " ").title()}</h2>'
        
        for topic, items in topics.items():
            html += f'<h3>{topic.replace("_", " ").title()}</h3>'
            
            for item in items:
                html += f"""
                <div class="req-item">
                    <h4>{item['file'].replace('.md', '')}</h4>
                    <div class="req-content">
                        {item['content']}
                    </div>
                </div>
                """
        
        html += '</div>'
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

def generate_stakeholders_html(stakeholders):
    """Generate HTML page for stakeholders"""
    # Group by category
    by_category = {}
    for sh in stakeholders:
        cat = sh['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(sh)
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stakeholders</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
            h1 { color: #0366d6; font-size: 2.5em; margin-bottom: 30px; border-bottom: 2px solid #0366d6; padding-bottom: 10px; }
            h2 { color: #24292e; font-size: 1.8em; margin-top: 30px; margin-bottom: 15px; }
            .stakeholder-card { background: white; padding: 20px; margin: 15px 0; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-top: 4px solid #28a745; }
            .stakeholder-name { color: #28a745; font-size: 1.3em; font-weight: bold; margin-bottom: 10px; }
            
            /* Custom styling for markdown content */
            .stakeholder-content { font-size: 0.95em; }
            .stakeholder-content h2 { font-size: 1.1em; color: #24292e; font-weight: 600; margin: 15px 0 8px 0; }
            .stakeholder-content h3 { font-size: 0.95em; color: #586069; font-weight: 600; margin: 12px 0 6px 0; }
            .stakeholder-content h4, .stakeholder-content h5, .stakeholder-content h6 { font-size: 0.9em; color: #666; font-weight: 600; margin: 10px 0 5px 0; }
            .stakeholder-content p { margin: 8px 0; }
            .stakeholder-content a { color: #0366d6; text-decoration: none; }
            .stakeholder-content a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Stakeholders</h1>
    """
    
    for category, sh_list in sorted(by_category.items()):
        html += f'<h2>{category.replace("_", " ").title()}</h2>'
        
        for sh in sh_list:
            html += f"""
            <div class="stakeholder-card">
                <div class="stakeholder-name">{sh['name'].replace('_', ' ').title()}</div>
                <div class="stakeholder-content">
                    {sh['content']}
                </div>
            </div>
            """
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

def main():
    # Create docs directory
    os.makedirs('docs', exist_ok=True)
    
    # Generate pages
    func_requirements = parse_func_requirements()
    nonfunc_requirements = parse_nonfunc_requirements()
    stakeholders = parse_stakeholders()
    
    funcreq_html = generate_func_requirements_html(func_requirements)
    nonfuncreq_html = generate_nonfunc_requirements_html(nonfunc_requirements)
    sh_html = generate_stakeholders_html(stakeholders)
    
    # Write files
    with open('docs/functional_requirements.html', 'w', encoding='utf-8') as f:
        f.write(funcreq_html)

    with open('docs/nonfunctional_requirements.html', 'w', encoding='utf-8') as f:
        f.write(nonfuncreq_html)
    
    with open('docs/stakeholder.html', 'w', encoding='utf-8') as f:
        f.write(sh_html)
    
    # Create index page
    index_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Documentation</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .container { text-align: center; color: white; }
            h1 { font-size: 3em; margin-bottom: 30px; }
            .link-grid { display: grid; grid-template-columns: repeat(2, 300px); gap: 20px; justify-content: center; }
            a { display: block; padding: 40px; background: white; color: #333; text-decoration: none; border-radius: 8px; font-size: 1.3em; font-weight: bold; transition: transform 0.3s; }
            a:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 Project Documentation</h1>
            <div class="link-grid">
                <a href="functional_requirements.html">Funktionale Anforderungen</a>
                <a href="nonfunctional_requirements.html">Nicht funktionale Anforderungen</a>
                <a href="stakeholder.html">Stakeholder</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print("✅ Documentation generated successfully!")

if __name__ == "__main__":
    main()