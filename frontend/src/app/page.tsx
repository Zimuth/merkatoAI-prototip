export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50 px-6">

      <section className="text-center max-w-2xl">

        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          MerkatoAI
        </h1>


        <p className="text-xl text-gray-600 mb-8">
          Marketplace inteligente con inteligencia artificial
          para automatizar la creación y gestión de productos.
        </p>


        <div className="flex gap-4 justify-center">

          <button
            className="
            px-6 py-3
            rounded-lg
            bg-black
            text-white
            hover:opacity-80
            "
          >
            Explorar productos
          </button>

          <button
            className="
            px-6 py-3
            rounded-lg
            border
            border-black
            text-black
            hover:bg-gray-100
            "
          >
            Crear cuenta
          </button>

        </div>

      </section>

    </main>
  );
}