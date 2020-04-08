async function send_and_expect_json(url)     {
    // const response = await fetch(`http://localhost:5000/`);
    console.log( "send_and_expect_json: " + url )
    const response = await fetch(url);
    const data = await response.json()
    return data;
}
async function send_and_expect_text(url)     {
    console.log( "send_and_expect_text: " + url )
    const response = await fetch(url);
    const data = await response.text()
    return data;
}