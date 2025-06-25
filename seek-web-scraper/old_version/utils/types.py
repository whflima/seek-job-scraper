from collections.abc import Buffer
from typing import Any, Mapping, TypeAlias

Parameters: TypeAlias = str | Buffer | int | float | Any | None | Mapping[str, str | Buffer | int | float | Any | None]

tech_stack_patterns = {
    "frontend": {
        "frameworks": r"\b(React|Angular|Vue|Svelte|Next\.js|Nuxt\.js|SolidJS|Qwik|Ember\.js|Backbone\.js|Preact)\b",
        "languages": r"\b(JavaScript|TypeScript|HTML|CSS|Dart)\b",
        "styling": r"\b(Tailwind CSS|Bootstrap|Material-UI|SASS|LESS|Styled Components|Emotion|Chakra UI|Ant Design)\b"
    },
    "backend": {
        "languages": r"\b(Java|Kotlin|Node\.js|Python|C#|Go|Ruby|Rust|PHP|Elixir|Scala)\b",
        "frameworks": r"\b(Spring Boot|J2EE|Express\.js|Django|Flask|\.NET Core|Ruby on Rails|FastAPI|Phoenix|Laravel|Symfony|Actix|Micronaut|Quarkus)\b",
        "j2ee_components": r"\b(EJB|JMS|JPA|Servlets|JSP|JSF|CDI)\b",
        "application_servers": r"\b(JBoss|WildFly|Apache Tomcat|WebLogic|GlassFish|Payara|Jetty|Resin)\b"
    },
    "cloud_infrastructure": {
        "providers": r"\b(Azure|AWS|Google Cloud Platform|IBM Cloud|Oracle Cloud|DigitalOcean|Heroku|Linode|Vercel|Netlify|Render)\b",
        "services": r"\b(Function Apps|Logic Apps|Lambda|Cloud Functions|App Engine|Step Functions|Cloud Run|Elastic Beanstalk)\b",
        "containers": r"\b(Docker|Podman|LXC|containerd|CRI-O)\b",
        "orchestration": r"\b(Kubernetes|Docker Swarm|Amazon ECS|OpenShift|Nomad|Rancher)\b",
        "devops": r"\b(CI/CD pipelines|Jenkins|GitHub Actions|GitLab CI|Azure DevOps|CircleCI|Travis CI|TeamCity|Bamboo|Spinnaker|Argo CD|Flux)\b"
    },
    "databases": {
        "types": r"\b(SQL|NoSQL|NewSQL|Graph|Time Series|Search Engine)\b",
        "sql_databases": r"\b(PostgreSQL|MySQL|SQL Server|Oracle DB|SQLite|MariaDB|CockroachDB|TiDB)\b",
        "nosql_databases": r"\b(MongoDB|Cassandra|DynamoDB|CouchDB|Redis|RethinkDB|Firebase Realtime Database|Amazon DocumentDB)\b",
        "graph_databases": r"\b(Neo4j|ArangoDB|Amazon Neptune|OrientDB|JanusGraph)\b"
    },
    "platforms": {
        "os": r"\b(Linux|Windows Server|macOS|FreeBSD|Ubuntu|Debian|RHEL|Alpine Linux)\b",
        "mobile": r"\b(iOS|Android|HarmonyOS|KaiOS|React Native|Flutter)\b"
    },
    "development_methodology": {
        "approach": r"\b(Agile|Scrum|Kanban|DevOps|Waterfall|XP|SAFe|Lean)\b",
        "team_structure": r"\b(Cross-functional|Feature teams|Squads|Guilds|Chapters|Tribes)\b"
    },
    "testing": {
        "unit_testing": r"\b(JUnit|Mockito|NUnit|Mocha|Jest|xUnit|pytest|unittest|RSpec|Catch2)\b",
        "e2e_testing": r"\b(Selenium|Cypress|Playwright|TestCafe|Nightwatch|Protractor|WebdriverIO)\b",
        "api_testing": r"\b(Postman|RestAssured|SoapUI|Karate|Insomnia|Pact|Dredd)\b"
    },
    "monitoring": {
        "tools": r"\b(Prometheus|Grafana|Datadog|New Relic|ELK Stack|Azure Monitor|Splunk|AppDynamics|Zabbix|Nagios|Sentry|CloudWatch)\b"
    },
    "version_control": {
        "tools": r"\b(Git|GitHub|GitLab|Bitbucket|Azure Repos|Subversion|Mercurial|Perforce)\b"
    },
    "collaboration_tools": {
        "tools": r"\b(Jira|Confluence|Slack|Microsoft Teams|Trello|Asana|ClickUp|Notion|Miro|Basecamp)\b"
    }
}

it_job_patterns = {
    "software_development": {
        "titles": r"\b(Software Developer|Software Engineer|Full Stack Developer|Frontend Developer|Backend Developer|Mobile Developer|Embedded Systems Engineer|Application Developer|Game Developer|Web Developer|Tech Lead|Solutions Architect|Software Architect)\b"
    },
    "data": {
        "titles": r"\b(Data Analyst|Data Scientist|Machine Learning Engineer|Data Engineer|BI Developer|Statistician|Data Architect|AI Engineer|Business Intelligence Analyst|Big Data Engineer|Quantitative Analyst|Research Data Scientist|Analytics Engineer|NLP Engineer)\b"
    },
    "cybersecurity": {
        "titles": r"\b(Security Analyst|Security Engineer|Penetration Tester|Ethical Hacker|SOC Analyst|Information Security Manager|CISO|Security Consultant|Incident Responder|Threat Analyst|Forensics Analyst|Application Security Engineer|Cybersecurity Architect|Vulnerability Analyst|IAM Specialist)\b"
    },
    "cloud_and_devops": {
        "titles": r"\b(DevOps Engineer|Site Reliability Engineer|Cloud Engineer|Platform Engineer|Infrastructure Engineer|Release Engineer|Cloud Solutions Architect|Cloud Consultant|Cloud Administrator|DevOps Architect|CI/CD Engineer|Automation Engineer|SRE)\b"
    },
    "networking": {
        "titles": r"\b(Network Engineer|Network Administrator|Systems Engineer|Telecom Engineer|Network Architect|Wireless Engineer|VoIP Engineer|Infrastructure Architect|NOC Engineer|Network Security Engineer)\b"
    },
    "it_support_and_admin": {
        "titles": r"\b(IT Support Specialist|System Administrator|Help Desk Technician|Desktop Support|IT Technician|Technical Support Analyst|IT Administrator|Service Desk Analyst|Field Service Technician|End-User Support Specialist|IT Operations Analyst|IT Coordinator)\b"
    },
    "project_and_product": {
        "titles": r"\b(IT Project Manager|Product Manager|Scrum Master|Program Manager|Agile Coach|Technical Program Manager|Product Owner|Delivery Manager|IT Portfolio Manager|Business Analyst|IT Business Partner)\b"
    },
    "qa_and_testing": {
        "titles": r"\b(QA Engineer|QA Analyst|Test Engineer|Automation Engineer|Software Tester|SDET|Performance Tester|Quality Engineer|Test Automation Architect|Manual Tester|Regression Tester|Load Tester|QA Lead)\b"
    },
    "ui_ux_and_design": {
        "titles": r"\b(UX Designer|UI Designer|Product Designer|Interaction Designer|Visual Designer|UX Researcher|UX/UI Developer|Design Lead|Information Architect|User Researcher|Motion Designer|Accessibility Specialist)\b"
    },
    "database": {
        "titles": r"\b(Database Administrator|DBA|Data Architect|Database Engineer|Database Analyst|SQL Developer|Data Warehouse Engineer|ETL Developer|Database Reliability Engineer)\b"
    },
    "ai_and_research": {
        "titles": r"\b(AI Engineer|NLP Engineer|Computer Vision Engineer|AI Researcher|Research Scientist|Deep Learning Engineer|Reinforcement Learning Engineer|AI Product Manager|Cognitive Computing Specialist|ML Ops Engineer|Conversational AI Engineer)\b"
    }
}