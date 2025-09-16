export default function Card({ title, children }) {
  return (
    <div className="bg-white shadow rounded-lg p-6 w-full">
      <h3 className="text-lg font-semibold mb-4">{title}</h3>
      <div>{children}</div>
    </div>
  );
}
