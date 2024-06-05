class WikiEngine:
    def __init__(self):
        self.documents = {}

    def create_document(self, title, content):
        if title in self.documents:
            print(f"Document '{title}' already exists.")
        else:
            self.documents[title] = content
            print(f"Document '{title}' created.")

    def edit_document(self, title, new_content):
        if title in self.documents:
            self.documents[title] = new_content
            print(f"Document '{title}' updated.")
        else:
            print(f"Document '{title}' does not exist.")

    def display_document(self, title):
        if title in self.documents:
            content = self.documents[title]
            print(f"Displaying document '{title}':")
            print(self._render_content(content))
        else:
            print(f"Document '{title}' does not exist.")

    def _render_content(self, content):
        # Replace internal links
        import re
        internal_link_pattern = r'\[\[([^\|\]]+)\|?([^\]]+)?\]\]'
        content = re.sub(internal_link_pattern, self._replace_internal_link, content)
        return content

    def _replace_internal_link(self, match):
        target = match.group(1)
        display_text = match.group(2) if match.group(2) else target
        return f"<a href='/wiki/{target}'>{display_text}</a>"

# Example usage
wiki = WikiEngine()

# Create documents
wiki.create_document("Python", "Python is a programming language.")
wiki.create_document("The Seed", "The Seed is a wiki engine. See [[Python|Python Programming Language]].")

# Edit a document
wiki.edit_document("The Seed", "The Seed is a powerful wiki engine. See [[Python]].")

# Display documents
wiki.display_document("Python")
wiki.display_document("The Seed")
