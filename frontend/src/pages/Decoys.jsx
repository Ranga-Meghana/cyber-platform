import Card from "../components/Card";

export default function Decoys() {
  return (
    <div className="p-6">
      <Card title="Deploy Decoys">
        <button className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
          Deploy New Decoy
        </button>
      </Card>
    </div>
  );
}
