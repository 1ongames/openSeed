import re

class TheSeedEngine:
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

    def delete_document(self, title):
        if title in self.documents:
            del self.documents[title]
            print(f"Document '{title}' deleted.")
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
        # Replace internal and external links
        internal_link_pattern = r'\[\[([^\|\]]+)\|?([^\]]+)?\]\]'
        external_link_pattern = r'\[\[(https?://[^\|\]]+)\|?([^\]]+)?\]\]'

        content = re.sub(external_link_pattern, self._replace_external_link, content)
        content = re.sub(internal_link_pattern, self._replace_internal_link, content)

        return content

    def _replace_internal_link(self, match):
        target = match.group(1)
        display_text = match.group(2) if match.group(2) else target
        return f"<a href='/wiki/{target}'>{display_text}</a>"

    def _replace_external_link(self, match):
        url = match.group(1)
        display_text = match.group(2) if match.group(2) else url
        return f"<a href='{url}'>{display_text}</a>"

# Example usage
wiki = TheSeedEngine()

# Create documents
wiki.create_document("Python", "Python is a programming language.")
wiki.create_document("The Seed", "The Seed is a wiki engine. See [[Python|Python Programming Language]] and [[https://www.google.com|Google]].")

# Edit a document
wiki.edit_document("The Seed", "The Seed is a powerful wiki engine. See [[Python]] and [[https://www.google.com]].")

# Delete a document
wiki.delete_document("Python")

# Display documents
wiki.display_document("The Seed")
