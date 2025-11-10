import React, { useEffect, useState } from "react";
import ApiScreen, { type ApiResponse } from "./ApiScreen";

const LoadingScreen: React.FC = () => (
  <div className="min-h-screen bg-gray-50 flex items-center justify-center">
    <div className="text-center">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500 mx-auto"></div>
      <p className="mt-4 text-gray-600">Loading...</p>
    </div>
  </div>
);

const ErrorScreen: React.FC<{ message: string; onRetry: () => void }> = ({
  message,
  onRetry,
}) => (
  <div className="min-h-screen bg-gray-50 flex items-center justify-center">
    <div className="text-center max-w-md">
      <div className="text-red-500 text-6xl mb-4">⚠️</div>
      <h2 className="text-2xl font-bold text-gray-900 mb-2">
        Something went wrong
      </h2>
      <p className="text-gray-600 mb-6">{message}</p>
      <button
        onClick={onRetry}
        className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-md font-medium transition-colors duration-200"
      >
        Try Again
      </button>
    </div>
  </div>
);

function QRPage() {
  // @ts-ignore
  const apiUrl = window._env_ // @ts-ignore
    ? window._env_.VITE_API_URL
    : import.meta.env.VITE_API_URL;

  // Extract ID from current URL path
  const getCurrentId = () => {
    const path = window.location.pathname;
    const segments = path.split("/").filter((segment) => segment !== "");
    return segments[segments.length - 1] || "";
  };

  const [currentId, setCurrentId] = useState(getCurrentId());
  const [data, setData] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const requestPage = async (pageId: string) => {
    try {
      setLoading(true);
      setError(null);

      const response = await fetch(`${apiUrl}${pageId}`);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const json = await response.json();
      setData(json);
    } catch (err) {
      console.error("API Error:", err);
      setError(err instanceof Error ? err.message : "Failed to load data");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    // Listen for URL changes (for SPA navigation)
    const handlePopState = () => {
      setCurrentId(getCurrentId());
    };

    window.addEventListener("popstate", handlePopState);

    // Initial load
    if (currentId) {
      requestPage(currentId);
    } else {
      setError("No ID provided in URL");
      setLoading(false);
    }

    return () => {
      window.removeEventListener("popstate", handlePopState);
    };
  }, [currentId]);

  const handleRetry = () => {
    if (currentId) {
      requestPage(currentId);
    }
  };

  if (loading) {
    return <LoadingScreen />;
  }

  if (error) {
    return <ErrorScreen message={error} onRetry={handleRetry} />;
  }

  if (!data) {
    return <ErrorScreen message="No data received" onRetry={handleRetry} />;
  }

  return (
    <>
      <nav className="navbar">
        <div className="container-fluid">
          <a
            className="navbar-brand"
            href="https://github.com/JustNevi/qr-page/"
          >
            <img
              src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"
              alt="Github logo"
              width="30"
              height="30"
            />
          </a>
        </div>
      </nav>
      <ApiScreen data={data} />;
    </>
  );
}

export default QRPage;
