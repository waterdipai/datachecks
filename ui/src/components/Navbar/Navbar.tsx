import React from "react";
import styles from "./Navbar.module.css";
import { navURLs } from "../../types/component.type";
import { BootstrapTooltip } from "../BootstrapTooltip";

const Navbar: React.FC = () => {
  return (
    <nav className={styles.navbar}>
      <div className={`datachecks_logo ${styles.logo}`} />
      <div className={styles.connects}>
        {navURLs.map((navURL, index) => (
          <BootstrapTooltip title={navURL.title}>
            <div
              key={index}
              className={styles.connect}
              onClick={() => window.open(navURL.url)}
            >
              <div className={`${navURL.logo} ${styles.logo}`} />
              {/* {navURL.title} */}
            </div>
          </BootstrapTooltip>
        ))}
      </div>
    </nav>
  );
};

export default Navbar;
