import AppList from '@/components/AppList'
import { Button } from '@/components/Button'
import { CallToAction } from '@/components/CallToAction'
import { Footer } from '@/components/Footer'
import { Header } from '@/components/Header'
import { Hero } from '@/components/Hero'
import { SearchInput } from '@/components/SearchInput'
import { appRouter } from '@/server/api/root'
import { prisma } from '@/server/db'
import type { GetStaticProps, InferGetServerSidePropsType } from 'next'
import * as R from 'ramda'
import { useState } from 'react'
import { useEffect } from 'react';


type App = {
  id: string
  name: string
  icon: string
  prompt: string
}
type PageProps = { apps: App[] }

export const getStaticProps: GetStaticProps<PageProps> = async () => {
  const caller = appRouter.createCaller({ prisma, session: null })
  const apps = await caller.app.getAll()

  return {
    props: {
      apps,
    },
    revalidate: 120, // In seconds
  }
}

const Home = (props: InferGetServerSidePropsType<typeof getStaticProps>) => {
  const { apps } = props
  const [searchValue, setSearchValue] = useState('')  // 钩子函数, 通过 setSearchValue函数来更新searchValue的值
  const [sizeToShow, setSizeToShow] = useState(12)  // 初始化显示APP个数
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:3000/sort', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ search_Value: searchValue }), // 传递 searchValue给Flask接口
        });

        if (response.ok) {
          const data = await response.json();// 设置获取到的列表数据
          console.log(data.type)
          setData(data);
          console.log(data)
        } else {
          console.error('Failed to fetch data from API');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, [searchValue]);

  // 匹配应用的prompt
  const list = searchValue
    ? apps.filter(app =>
      [data[0], data[1], data[2], data[3], data[4]].some(value =>
        app.prompt.includes(value)
      )
    )
    : apps;

  const handleShowMore = () => {
    setSizeToShow(sizeToShow + 100)
  }

  return (
    <>
      <Header />
      <main>
        <Hero />
        <div className="w-full bg-slate-50 pb-20 pt-10">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="mb-10 grid grid-cols-1 items-center justify-between pt-10 sm:grid-cols-3 sm:pt-0 ">
              <div />
              <SearchInput
                setSearchValue={setSearchValue}
                placeholder={`Search ${apps.length} apps...`}
              />
              <div />
            </div>
            <AppList list={R.take(sizeToShow, list)} />

            <div className="mt-10 flex justify-center">
              <Button color="blue" onClick={handleShowMore}>
                加载更多
              </Button>
            </div>
          </div>
        </div>
        {/* <PrimaryFeatures /> */}
        {/* <SecondaryFeatures /> */}
        <CallToAction />
        {/* <Testimonials /> */}
        {/* <Pricing /> */}
        {/* <Faqs /> */}
      </main>
      <Footer />
    </>
  )
}

export default Home
