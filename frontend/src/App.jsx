
import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [description, setDescription] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setDescription(data.description);
  };

  return (
    <div>
      <h1>Visor de imágenes SAR + LLM</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Subir imagen</button>
      <p><strong>Descripción:</strong> {description}</p>
    </div>
  );
}

export default App;
