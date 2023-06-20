import Link from 'next/link'

export const NavLink = ({
  href,
  children,
}: {
  href: string
  children?: React.ReactNode
}) => {
  return (
    <Link
      href={href}
      className="inline-block rounded-lg py-1 px-2 text-sm text-slate-700 hover:"
      style={{ color: 'white', fontSize: '16px', fontWeight: '600', wordSpacing: '3px', display: 'block', height: '60px', lineHeight: '60px', padding: '0' }}
      onMouseEnter={(e) => {
        e.target.style.color = 'rgb(0,0,139)';
      }}
      onMouseLeave={(e) => {
        e.target.style.color = 'white';
      }}
    >
      {children}
    </Link>
  )
}
