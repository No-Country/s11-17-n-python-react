import PropTypes from "prop-types";
import AppLink from "../../UI/AppLink";

/**
 * Generates a card icon component.
 *
 * @param {string} className - The CSS class name for the card icon.
 * @param {string} icon - The icon class for the card icon bootstrap.
 * @param {boolean} iconAbove - Determines whether the icon is placed above the title.
 * @param {string} title - The title of the card icon.
 * @param {string} text - The text content of the card icon.
 * @param {object} link - The link object containing the URL and text for the card icon.
 * @return {JSX.Element} The card icon component.
 */
const CardIcon = ({ className, icon, iconAbove, title, text, link }) => {
  const iconClass = !iconAbove ? "d-flex align-items-center" : "";
  return (
    <div className={`card ${className}`}>
      <div className="card-body">
        <div className={iconClass}>
          <div className="mb-2">
            <span>
              <i className={icon} style={{ fontSize: "2em" }}></i>
            </span>
          </div>
          {title && (
            <h6 className={`card-title m-0 ${!iconAbove ? "ms-2" : ""}`}>
              {title}
            </h6>
          )}
        </div>

        {text && <p className="card-text m-0">{text}</p>}
        {link && (
          <AppLink href={link.url} className="small">
            {link.text}{" "}
            <i
              className="bi bi-chevron-right"
              style={{ fontSize: "0.7em" }}
            ></i>
          </AppLink>
        )}
      </div>
    </div>
  );
};

CardIcon.propTypes = {
  className: PropTypes.string,
  icon: PropTypes.string,
  iconAbove: PropTypes.bool,
  title: PropTypes.string,
  text: PropTypes.string,
  link: PropTypes.object,
};

export default CardIcon;
