import React, { useState, useRef, useEffect } from "react";
import { FaBars } from "react-icons/fa";
import { links, social } from "./data";
import classes from "./Navbar.module.css";
import logo from "./favicon.svg";

const Navbar = () => {
  const [showLinks, setShowLinks] = useState(false);
  const linksContainerRef = useRef(null);
  const linksRef = useRef(null);
  const toggleLinks = () => {
    setShowLinks(!showLinks);
  };
  useEffect(() => {
    const linksHeight = linksRef.current.getBoundingClientRect().height;
    if (showLinks) {
      linksContainerRef.current.style.height = `${linksHeight}px`;
    } else {
      linksContainerRef.current.style.height = "0px";
    }
  }, [showLinks]);
  return (
    <nav>
      <div className={classes.navCenter}>
        <div className={classes.navHeader}>
          <img src={logo} className={classes.logo} alt="logo" />
          <button className={classes.navToggle} onClick={toggleLinks}>
            <FaBars />
          </button>
        </div>
        <div className={classes.linksContainer} ref={linksContainerRef}>
          <ul className={classes.links} ref={linksRef}>
            {links.map((link) => {
              const { id, url, text } = link;
              return (
                <li key={id}>
                  <a href={url} className="scroll-link">
                    {text}{" "}
                  </a>
                </li>
              );
            })}
          </ul>
        </div>
        <ul className={classes.socialIcons}>
          {social.map((socialIcon) => {
            const { id, url, icon } = socialIcon;
            return (
              <li key={id}>
                <a href={url} target="_blank" rel="noopener noreferrer">
                  {icon}
                </a>
              </li>
            );
          })}
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
