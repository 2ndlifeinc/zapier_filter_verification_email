
import urllib.request


url = "https://raw.githubusercontent.com/2ndlifeinc/zapier_filter_verification_email/refs/heads/main/zapier_filter_verification_email.py"
with urllib.request.urlopen(url) as response:
    code = response.read().decode('utf-8')

namespace = {}
exec(code, namespace)

filter_func = namespace['filter_func']
test_input = {
    'subject': 'Please verify your email address',
    'body_html': '<a href="https://example.com/verify">Click here to verify</a>',
    'from': 'noreply@example.com'
}
print(filter_func(test_input))
