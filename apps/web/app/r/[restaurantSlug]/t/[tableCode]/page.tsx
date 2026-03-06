type PageProps = {
  params: {
    restaurantSlug: string;
    tableCode: string;
  };
};

export default function TableExperiencePage({ params }: PageProps) {
  return (
    <main>
      <div className="card">
        <h1>{params.restaurantSlug}</h1>
        <p>Mesa: {params.tableCode}</p>
      </div>

      <div className="card">
        <h2>¿Qué quieres hacer?</h2>
        <p>Flujo MVP: menú, juego, voto y ranking diario.</p>
        <button className="button" type="button">
          Ver menú
        </button>
      </div>
    </main>
  );
}
