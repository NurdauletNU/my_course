import * as bases from "../components/bases";
import { Link } from "react-router-dom";

export default function Page() {
  return (
    <bases.Base1>
      <div
        className="bg-dark text-secondary px-4 py-5 text-center"
        style={{
          backgroundImage:
            'url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIO0HGkCyIik71Gz2AfkGzAizo4aLTeAj_ZM-d1lxOqA&s")',
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundRepeat: "no-repeat",
        }}
      >
        <div
          className="py-5"
          style={{
            backgroundColor: "rgba(0, 0, 0, 0.5)",
            borderRadius: "10px",
          }}
        >
          <h1 className="display-5 fw-bold text-white mb-4">
            Интересный мир книг
          </h1>
          <div className="col-lg-6 mx-auto">
            <p className="fs-5 text-white mb-4">
              Раскройте для себя увлекательный мир книг с нашим книжным
              магазином. Мы предлагаем широкий выбор литературы на любой вкус и
              интересы.
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
              <Link
                to="/BookList"
                className="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold"
              >
                Список книг
              </Link>
              <button
                type="button"
                className="btn btn-outline-light btn-lg px-4"
              >
                Вперёд к чтению
              </button>
            </div>
          </div>
        </div>
      </div>
    </bases.Base1>
  );
}
