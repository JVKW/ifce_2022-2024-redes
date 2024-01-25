import { Link } from "react-router-dom";

import { useAuthValue } from "../../contexts/AuthContext";

// CSS
import styles from "./About.module.css";

const About = () => {
  const { user } = useAuthValue();

  return (
    <div className={styles.about}>
      <h2>
        Sobre o Mini <span>Blog</span>
      </h2>
      <p>
        Este projeto consiste em um blog feito com React no front-end e Firebase
        no back-end.
      </p>
      {user ? (
        <Link to="/posts/create" className="btn">
          Criar post
        </Link>
      ) : (
        <Link to="/login" className="btn">
          Entrar
        </Link>
      )}
    </div>
  );
};

export default About;
