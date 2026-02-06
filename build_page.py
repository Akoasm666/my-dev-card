def main():
    # 个人信息配置
    personal_info = {
        "name": "陈鹏舟(Pengzhou Chen)",
        "title": "Software Engineer @ AMMO AI | B.S. in CS, University of Michigan",
        "description": "Full-stack Software Engineer with experience in AI-powered applications, "
                       "Django REST Framework, multi-agent systems, and vector database search. "
                       "Passionate about building scalable backend systems, MLOps, and CI/CD automation.",
        "skills": [
            "Python", "Java", "C++", "JavaScript", "TypeScript",
            "Django", "Flask", "FastAPI", "React",
            "PostgreSQL", "MongoDB", "VectorDB", "Elasticsearch",
            "Docker", "Git", "CI/CD", "Jenkins",
            "AWS", "GCP", "Microsoft Azure",
            "REST Framework", "WebSocket", "Pytorch"
        ],
        "projects": [
            {
                "name": "AMMO AI - Multi-Agent AI Application",
                "description": "Built a Django REST backend with multi-agent architecture, "
                               "pgvector semantic search, and WebSocket real-time communication. "
                               "Deployed via Docker on Google Cloud Run, reaching 70k users in 2 weeks."
            },
            {
                "name": "Vision-Based Cancer Detection Using Deep Learning",
                "description": "Designed a multi-layer CNN model on 100,000+ cancer images achieving 80% accuracy. "
                               "Created a chatbot for cancer prediction and care advice. Published at SPIE."
            },
            {
                "name": "HireBeat - GitHub Profile Chrome Extension",
                "description": "Developed a Chrome Extension to scrape GitHub profiles for 50+ employers. "
                               "Full-stack system with React/JQuery frontend and Python Flask + PostgreSQL backend."
            },
            {
                "name": "Database Migration for Social Media Platform",
                "description": "Redesigned database schemas for an Instagram-like platform. "
                               "Migrated data from Oracle DB to MySQL and MongoDB using SQL and NoSQL queries."
            }
        ],
        "contact": {
            "github": "https://github.com/Akoasm666",
            "linkedin": "https://www.linkedin.com/in/pengzhou-chen-a52b60195/"
        }
    }

    # HTML 模板
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{personal_info['name']} - Tech Card</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    line-height: 1.6;
    background-color: #f4f4f4;
}}
.container {{
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}}
h1 {{
    color: #333;
    text-align: center;
    margin-bottom: 10px;
}}
.title {{
    text-align: center;
    color: #666;
    font-size: 1.2em;
    margin-bottom: 20px;
}}
.skills {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 20px 0;
}}
.skill {{
    background: #007bff;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9em;
}}
.projects, .contact {{
    margin: 20px 0;
}}
a {{
    color: #007bff;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
</style>
</head>
<body>
<div class="container">
<h1>{personal_info['name']}</h1>
<div class="title">{personal_info['title']}</div>
<p>{personal_info['description']}</p>
<h2>技能</h2>
<div class="skills">
"""
    # 添加技能标签
    for skill in personal_info['skills']:
        html_content += f'    <span class="skill">{skill}</span>\n'
    html_content += """
</div>
<h2>项目经历</h2>
<div class="projects">
<ul>
"""
    # 添加项目描述
    for project in personal_info['projects']:
        html_content += f'    <li><strong>{project["name"]}</strong>: {project["description"]}</li>\n'
    html_content += f"""
</ul>
</div>
<h2>联系方式</h2>
<div class="contact">
<p>
<a href="{personal_info['contact']['github']}" target="_blank">GitHub</a> |
<a href="{personal_info['contact']['linkedin']}" target="_blank">LinkedIn</a>
</p>
</div>
</div>
</body>
</html>
"""

    # 写入文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("index.html generated successfully!")


if __name__ == "__main__":
    main()
