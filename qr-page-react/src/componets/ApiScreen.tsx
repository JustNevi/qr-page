import React from "react";

export interface RedirectButton {
  redirect_url: string;
  text: string;
  icon_url: string;
}

export interface ApiResponse {
  title: string;
  image_url: string;
  id: number;
  redirect_buttons: RedirectButton[];
}

interface ApiScreenProps {
  data?: ApiResponse;
}

const ApiScreen: React.FC<ApiScreenProps> = ({
  data = {
    title: "TITLE",
    image_url:
      "https://via.placeholder.com/200x200/e5e7eb/6b7280?text=Main+Logo",
    id: 1,
    redirect_buttons: [
      {
        redirect_url: "#",
        text: "TEXT",
        icon_url: "https://via.placeholder.com/24x24/3b82f6/ffffff?text=🔗",
      },
      {
        redirect_url: "#",
        text: "TEXT",
        icon_url: "https://via.placeholder.com/24x24/3b82f6/ffffff?text=🔗",
      },
      {
        redirect_url: "#",
        text: "TEXT",
        icon_url: "https://via.placeholder.com/24x24/3b82f6/ffffff?text=🔗",
      },
    ],
  },
}) => {
  return (
    <>
      <h1 className="text-center"> {data.title} </h1>
      <div className="text-center my-4">
        <img
          src={data.image_url}
          className="img-fluid"
          style={{ maxWidth: "100%", height: "auto" }}
          alt="Main logo"
        />
      </div>
      <ul className="list-group">
        {data.redirect_buttons.map((button, index) => (
          <li
            key={index}
            className="list-group-item d-flex justify-content-center"
          >
            <div className="d-flex align-items-center">
              <img src={button.icon_url} className="me-2" alt="Redirect logo" />
              <a
                href={button.redirect_url}
                target="_blank" // Opens the URL in a new tab/window
                rel="noopener noreferrer" // Recommended for security when using target="_blank"
                className="btn btn-primary" // Apply Bootstrap button styling
              >
                {button.text}
              </a>
            </div>
          </li>
        ))}
      </ul>
    </>
  );
};

export default ApiScreen;
