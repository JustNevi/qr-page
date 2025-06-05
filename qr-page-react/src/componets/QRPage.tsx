import { useEffect } from "react";

function QRPage() {
  const requestPage = () => {
    fetch(import.meta.env.VITE_API_URL + "1")
      .then((response) => response.json())
      .then((json) => console.log(json));
  };

  useEffect(() => {
    requestPage();
  });

  return <div></div>;
}

export default QRPage;
