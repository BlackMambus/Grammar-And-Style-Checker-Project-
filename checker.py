import language_tool_python

# Initialize the grammar checker
tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    # Get list of grammar issues
    matches = tool.check(text)

    # Display issues
    print(f"\n🔍 Found {len(matches)} issues:\n")
    for match in matches:
        print(f"✏️ Issue: {match.message}")
        print(f"   Suggestion: {match.replacements}")
        print(f"   Context: {match.context}")
        print(f"   Rule: {match.ruleId}\n")

    # Return corrected version
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

# Example usage
if __name__ == "__main__":
    sample_text = input("Enter text to check:\n")
    corrected = check_grammar(sample_text)
    print("\n✅ Corrected Text:\n")
    print(corrected)


