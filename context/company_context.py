from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

def get_company_context():
    about_company = "Gamed Gamed is a company that provides AI solutions to help websites refine their search and recommendation systems."
    return StringKnowledgeSource(content=about_company)
