function runDebugger() {
    const language = document.getElementById('language').value;
    const code = document.getElementById('code').value;
    const output = document.getElementById('output');

    fetch('/debug', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language, code })
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.output;
    })
    .catch(err => {
        output.textContent = 'Error: ' + err;
    });
}
