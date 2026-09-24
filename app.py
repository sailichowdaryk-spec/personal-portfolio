from flask import Flask, render_template, abort

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Content — edit this to update the site. Nothing else needs to change.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Saili Chowdary Kamsani",
    "tagline": "CSE student building at the intersection of ML, vision, and full-stack products.",
    "location": "Hyderabad, India",
    "bio": (
        "I'm a second-year CSE student who likes taking a project from a research "
        "paper to something that actually runs — whether that's a detector trained "
        "on underwater trash, a vector-search tool for classifying complaints, or "
        "a small business website with its own hand-built design system. My work "
        "spans machine learning, NLP, computer vision, and full-stack development "
        "with React and Flask."
    ),
    "highlights": [
        {"label": "Internship", "value": "Data Science Intern at IDEAS-TIH, Indian Statistical Institute Kolkata ," 
        "AIML Research intern at IIT Ghuwahati "},
        {"label": "Focus areas", "value": "Machine Learning · Computer Vision · NLP · Full-stack (React, Flask)"},
        {"label": "Currently", "value": "Training YOLO11n on the TrashCan dataset for underwater garbage detection"},
    ],
    "skills": {
        "Machine Learning & CV": ["PyTorch", "YOLO / Faster R-CNN", "OpenCV", "Dataset auditing & EDA"],
        "NLP": ["Transformers.js", "Hugging Face models", "Sentence embeddings", "Vector search"],
        "Full-stack": ["React 19 + Vite", "Flask", "Node.js / Express", "MongoDB Atlas", "SQLite"],
        "Tools": ["Git/GitHub", "Google Colab", "ngrok", "Jupyter"],
    },
    "contact": {
        "email": "sailichowdaryk@gmail.com",
        "github": "https://github.com/sailichowdaryk-spec",
        "linkedin": "https://www.linkedin.com/in/saili-chowdary-kamsani-9bb23937b/?isSelfProfile=true",
    },
}

PROJECTS = [
    {
        "slug": "underwater-garbage-detection",
        "title": "Underwater Garbage Detection",
        "blurb": "A computer-vision pipeline that detects underwater trash using the TrashCan dataset.",
        "tags": ["Computer Vision", "PyTorch", "YOLO"],
        "featured": True,
        "description": (
            "An ongoing, structured computer-vision project to detect and localize "
            "garbage in underwater imagery, built as a day-by-day sequence of "
            "deliverables rather than a single monolithic build."
        ),
        "details": [
            "Built a COCO-format dataset-auditing toolkit and ran exploratory data analysis on the TrashCan dataset.",
            "Designed a preprocessing pipeline with leakage-safe train/val/test splits and a SHA-256 dataset freeze for reproducibility.",
            "Ran detector experiments comparing Faster R-CNN against MobileNetV3 variants.",
            "Pivoted the modeling plan to YOLO11n (250 epochs), replacing an earlier YOLOv8s approach.",
            "Synthesized research across five YOLO / Faster R-CNN papers into a full project plan, plus PowerPoint decks for mentor reviews.",
            "Worked through recurring real-world friction: PowerShell environment quirks, numpy version conflicts, Jupyter PATH issues, YAML errors, and OOM kernel kills during training.",
        ],
        "stack": ["Python", "PyTorch", "OpenCV", "YOLO11n", "Jupyter"],
    },
    {
        "slug": "sociohood",
        "title": "Sociohood — Complaint Categorization",
        "blurb": "A tool that classifies resident complaints using sentence embeddings and vector search.",
        "tags": ["NLP", "React", "Vector Search"],
        "featured": True,
        "description": (
            "A complaint-categorization system built for a residential township, pairing "
            "a lightweight in-browser embedding model with a vector-search backend."
        ),
        "details": [
            "Built the frontend in React 19 + Vite, running bge-small-en-v1.5 embeddings client-side via Transformers.js.",
            "Generated vector embeddings for roughly 1,600 complaint subcategories and indexed them in MongoDB Atlas with a vector search index.",
            "Authored complaint-description data for the Tata Motors Township subcategory set.",
            "Presented the frontend architecture and testing approach for an academic review.",
        ],
        "stack": ["React 19", "Vite", "Transformers.js", "MongoDB Atlas"],
    },
    {
        "slug": "freshseal",
        "title": "FreshSeal",
        "blurb": "A hardware/software startup concept, taken from market research through to pitch deck.",
        "tags": ["Startup", "Market Research", "Pitch Deck"],
        "featured": True,
        "description": (
            "A hardware/software product concept developed end-to-end: market analysis, "
            "funding strategy, and pitch materials for a jury audience."
        ),
        "details": [
            "Wrote an investment plan with an India-specific funding roadmap: Startup India Seed Fund, NIDHI, and TIDE 2.0.",
            "Produced a competitive-landscape analysis and identified RO water purifiers as the closest Indian market analogy.",
            "Designed a pitch deck (forest green / amber palette) and wrote a one-minute pitch script with jury Q&A prep.",
        ],
        "stack": ["Market Research", "Financial Planning", "PowerPoint"],
    },
    {
        "slug": "minedrop",
        "title": "MineDrop",
        "blurb": "A redesigned Minecraft server website with a custom admin dashboard.",
        "tags": ["Full-stack", "Node.js", "Design"],
        "featured": False,
        "description": (
            "A visual refresh and admin tooling build for a Minecraft server's website."
        ),
        "details": [
            "Redesigned multiple pages into a modern design system using Space Grotesk with lime, orange, and purple accents.",
            "Built a Node.js + Express + SQLite admin dashboard with session-based authentication.",
        ],
        "stack": ["Node.js", "Express", "SQLite"],
    },
    {
        cat << 'EOF'
    {
        "slug": "nlp-web-app",
        "title": "Multi-Model NLP Web App",
        "blurb": "A Flask app serving three Hugging Face NLP models through one interface.",
        "tags": ["NLP", "Flask", "Hugging Face"],
        "featured": False,
        "description": (
            "A web app built in Google Colab that hosts three Hugging Face models "
            "behind a single embedded frontend, tunneled out with ngrok."
        ),
        "details": [
            "Served sentiment analysis, summarization, and zero-shot classification models through one Flask backend.",
            "Built a fully embedded HTML frontend within the same Colab notebook.",
            "Resolved torch/torchvision version mismatches and ngrok tunnel conflicts during deployment.",
        ],
        "stack": ["Flask", "Hugging Face Transformers", "ngrok", "Google Colab"],
    },
    {
        "slug": "terrawatch",
        "title": "TerraWatch — Landslide Early Warning System",
        "blurb": "A prototype dashboard that scores landslide risk in real time from rainfall and soil-moisture inputs.",
        "tags": ["Data Viz", "JavaScript", "Simulation"],
        "featured": True,
        "description": (
            "A Smart India Hackathon (SIH26001) prototype for an early-warning system: "
            "an interactive risk map paired with a transparent, explainable scoring engine, "
            "built to run entirely offline for demos with no live backend required."
        ),
        "details": [
            "Built an interactive Leaflet.js risk map with grid cells that recolor live (low / watch / warning / danger) as conditions change.",
            "Designed a risk-scoring engine combining rainfall intensity, rainfall duration, antecedent rainfall, and soil moisture, with an explainability panel breaking the score into each factor's contribution.",
            "Added role-based views (district officer, admin, citizen) that show or hide the threshold-tuning and citizen-reporting panels accordingly.",
            "Built an admin panel for live-tuning yellow/orange/red alert thresholds, backed by a six-check automated self-test suite verifying monotonicity, score capping, and contribution-share accuracy.",
            "Added a storm-replay mode and quick scenario presets (calm/watch/warning/danger) plus a citizen ground-report feature for logging on-map observations, so the whole demo runs client-side.",
        ],
        "stack": ["JavaScript", "Leaflet.js", "Chart.js", "HTML/CSS"],
    },
]
}

def get_project_or_404(slug):
    for project in PROJECTS:
        if project["slug"] == slug:
            return project
    abort(404)


@app.route("/")
def index():
    featured = [p for p in PROJECTS if p["featured"]]
    return render_template("index.html", profile=PROFILE, projects=featured)


@app.route("/projects")
def projects():
    return render_template("projects.html", profile=PROFILE, projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = get_project_or_404(slug)
    return render_template("project_detail.html", profile=PROFILE, project=project)


@app.route("/about")
def about():
    return render_template("about.html", profile=PROFILE)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", profile=PROFILE), 404


if __name__ == "__main__":
    app.run(debug=True)
