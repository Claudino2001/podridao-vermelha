document.getElementById('uploadForm').onsubmit = async function (event) {
    event.preventDefault();

    const formData = new FormData();
    const imageInput = document.getElementById('imageInput');
    formData.append('file', imageInput.files[0]);

    try {
        const response = await fetch('http://localhost:5000/detecta-fungo', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('result').innerText =
                `Classe: ${result.class}\nConfiança: ${result.confidence}`;
        } else {
            document.getElementById('result').innerText =
                'Erro ao processar a imagem. Tente novamente.';
        }
    } catch (error) {
        document.getElementById('result').innerText =
            'Erro de conexão com o servidor. Verifique se o serviço está ativo.';
    }
};
