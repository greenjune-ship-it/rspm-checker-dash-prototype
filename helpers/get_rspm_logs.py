def rspm_call(content):
    # the function to call from shell
    pass


def format_markdown(content):
    return f'''
    ```bash
    rspm list git-builder {content}
    rspm logs --transaction-id=123456
    ```
    '''
