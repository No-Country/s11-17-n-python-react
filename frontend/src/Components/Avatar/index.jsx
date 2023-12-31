import React from "react";
import PropTypes from "prop-types";
import avatarImage from "../../assets/blank.png";
import styles from "./Avatar.module.css";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import AppLink from "../../UI/AppLink";

const Avatar = ({ imageUrl }) => {
  imageUrl = imageUrl || avatarImage;

  const navigate = useNavigate();
  const cuenta = JSON.parse(localStorage.getItem("logedAccount"));

  const handleLogout = () => {
    localStorage.removeItem("logedAccount");
    Cookies.remove("authToken");
    Cookies.remove("userId");
    setTimeout(() => {
      navigate("/");
      location.reload();
    }, 500);
  };

  return (
    <div className="dropdown ms-2 btn cursor-pointer">
      <img
        src={imageUrl}
        className={`img-fluid rounded-circle ${styles.avatar}`}
        id="avatarDropdown"
        data-bs-toggle="dropdown"
        alt="avatar"
      />
      <ul
        className="dropdown-menu dropdown-menu-end"
        aria-labelledby="avatarDropdown"
      >
        <li>
          <p className="dropdown-item text-primary">{cuenta}</p>
          <AppLink className="dropdown-item" href="/profile">
            Mi Perfil
          </AppLink>
        </li>
        <li>
          <button className="dropdown-item text-danger" onClick={handleLogout}>
            Cerrar Sesión
          </button>
        </li>
      </ul>
    </div>
  );
};

Avatar.propTypes = {
  imageUrl: PropTypes.string,
};

export default Avatar;
