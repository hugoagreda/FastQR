import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "FastQR",
  description: "Interactive QR experience for restaurant tables"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
