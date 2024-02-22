import * as bases from "../components/bases";

export default function Page() {
  return (
    <bases.Base1>
      <div className="container py-5">
        <div className="row">
          <div className="col-lg-8 mx-auto">
            <h2 className="text-center mb-4">Часто задаваемые вопросы</h2>

            <p className="about-text">
              Добро пожаловать в наш книжный магазин! Мы гордимся тем, что
              предлагаем широкий ассортимент книг на любой вкус и интересы.
            </p>

            <h3 className="mt-5">Часто задаваемые вопросы</h3>
            <div className="faq-item">
              <h4>Каковы ваши способы оплаты?</h4>
              <p>
                Мы принимаем к оплате кредитные карты, PayPal и банковские
                переводы.
              </p>
            </div>
            <div className="faq-item">
              <h4>Каковы ваши условия возврата?</h4>
              <p>
                Мы принимаем возврат товара в течение 30 дней после покупки при
                условии сохранения товарного вида.
              </p>
            </div>
            <div className="faq-item">
              <h4>Как я могу отследить мою посылку?</h4>
              <p>
                После оформления заказа вы получите электронное письмо с
                информацией о трекинге вашей посылки.
              </p>
            </div>
          </div>
        </div>
      </div>
    </bases.Base1>
  );
}
