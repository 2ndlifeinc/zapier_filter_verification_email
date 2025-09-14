import re


subject = input_data.get('subject', '')
subject_verify_keywords = [
    "verification",
    "verify",
    "인증",
    "Authentication code",
    "login code",
    "login",
    "Log In",
    "code",
    "코드",
    "Secure link",
    "로그인",
    "보안 링크",
    "Activate",
]
subject_additional_filtering_keywords = [
    "한국전자인증",
]


def get_included_keyword(target, keywords):
    if not target:
        return None

    for each in keywords:
        if not each:
            continue
        if each.lower() in target.lower():
            return each
    return None


ret = {
    "is_verification_email": False,
}
for key, val in input_data.items():
    ret[key] = val


subject = subject.lower()
included_subject_verify_keyword = get_included_keyword(subject, subject_verify_keywords)
if not included_subject_verify_keyword:
    return ret
if get_included_keyword(subject, subject_additional_filtering_keywords):
    return ret

ret["subject_keyword"] = included_subject_verify_keyword
ret["is_verification_email"] = True


def extract_link_contents(target_html):
    links = []
    if not target_html:
        return links
    href_links = re.findall(r'href=[\'"]?([^\'" >]+)', body_html)
    for link in href_links:
        if not re.search(r'\.(jpg|jpeg|png|gif|svg|css|ico)(\?|$)', link, re.IGNORECASE) \
                and not '/static/' in link \
                and not '/assets/' in link \
                and not link.startswith('mailto:') \
                and not link.startswith('javascript:'):
            links.append(link)
    return links


ret["body_links"] = ""
if 'body_html' in ret:
    body_html = ret['body_html']
    ret.pop("body_html")
    ret["body_links"] = "\n".join(extract_link_contents(body_html))

return ret
