'use client';

import { useState } from 'react';

export default function Page() {
    const [activeTab, setActiveTab] = useState('overview');

    return (
        <div
            className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white"
            data-oid="8fnzc1d"
        >
            {/* Header */}
            <header
                className="border-b border-purple-800/30 backdrop-blur-sm bg-black/20"
                data-oid="fqkxwmp"
            >
                <div
                    className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center"
                    data-oid="w0z-mav"
                >
                    <div className="flex items-center space-x-2" data-oid="-uu0fvy">
                        <div
                            className="w-8 h-8 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center"
                            data-oid="me0z.b2"
                        >
                            <span className="text-white font-bold text-sm" data-oid="487e-60">
                                AI
                            </span>
                        </div>
                        <span className="text-xl font-semibold" data-oid="i-ifrkb">
                            AgentPro
                        </span>
                    </div>
                    <nav className="hidden md:flex space-x-8" data-oid="ojh.i16">
                        <a
                            href="#"
                            className="text-gray-300 hover:text-white transition-colors"
                            data-oid="tigr3e-"
                        >
                            Features
                        </a>
                        <a
                            href="#"
                            className="text-gray-300 hover:text-white transition-colors"
                            data-oid="j.h2cvs"
                        >
                            Pricing
                        </a>
                        <a
                            href="#"
                            className="text-gray-300 hover:text-white transition-colors"
                            data-oid="j6s6c5s"
                        >
                            Docs
                        </a>
                    </nav>
                    <div className="flex space-x-4" data-oid="eczws4x">
                        <button
                            className="px-4 py-2 text-gray-300 hover:text-white transition-colors"
                            data-oid="huzw1mk"
                        >
                            Sign In
                        </button>
                        <button
                            className="px-6 py-2 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg hover:from-purple-700 hover:to-pink-700 transition-all"
                            data-oid="c2qeftq"
                        >
                            Get Started
                        </button>
                    </div>
                </div>
            </header>

            {/* Hero Section */}
            <section className="max-w-7xl mx-auto px-6 py-20" data-oid="xbprmv3">
                <div className="text-center mb-16" data-oid="6bisu66">
                    <h1
                        className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-transparent"
                        data-oid="c9vybvl"
                    >
                        Your AI Agent
                        <br data-oid="x-c65a8" />
                        <span className="text-4xl md:text-6xl" data-oid="5s1-xo0">
                            Dashboard
                        </span>
                    </h1>
                    <p className="text-xl text-gray-300 max-w-3xl mx-auto mb-8" data-oid="4j89s--">
                        Monitor, control, and optimize your AI agents with real-time analytics,
                        intelligent insights, and seamless automation tools.
                    </p>
                    <button
                        className="px-8 py-4 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl text-lg font-semibold hover:from-purple-700 hover:to-pink-700 transition-all transform hover:scale-105"
                        data-oid="z7aj05h"
                    >
                        Launch Dashboard
                    </button>
                </div>

                {/* Dashboard Preview */}
                <div
                    className="bg-black/40 backdrop-blur-sm border border-purple-800/30 rounded-2xl p-6 shadow-2xl"
                    data-oid="0kt:18g"
                >
                    {/* Dashboard Header */}
                    <div className="flex justify-between items-center mb-6" data-oid="m031_ga">
                        <h2 className="text-2xl font-semibold w-[190px]" data-oid="m7byzyc">
                            Agent Dashboard
                        </h2>
                        <div className="flex space-x-2" data-oid="5tzeyr1">
                            <div
                                className="w-3 h-3 bg-red-500 rounded-full"
                                data-oid=":94yhvd"
                            ></div>
                            <div
                                className="w-3 h-3 bg-yellow-500 rounded-full"
                                data-oid="h-e988x"
                            ></div>
                            <div
                                className="w-3 h-3 bg-green-500 rounded-full"
                                data-oid="1iwdyud"
                            ></div>
                        </div>
                    </div>

                    {/* Dashboard Tabs */}
                    <div
                        className="flex space-x-1 mb-6 bg-gray-800/50 rounded-lg p-1"
                        data-oid=":ii-2bk"
                    >
                        {['overview', 'agents', 'analytics', 'settings'].map((tab) => (
                            <button
                                key={tab}
                                onClick={() => setActiveTab(tab)}
                                className={`px-4 py-2 rounded-md capitalize transition-all ${
                                    activeTab === tab
                                        ? 'bg-purple-600 text-white'
                                        : 'text-gray-400 hover:text-white'
                                }`}
                                data-oid="wv2fnd3"
                            >
                                {tab}
                            </button>
                        ))}
                    </div>

                    {/* Dashboard Content */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6" data-oid="d6nfb-i">
                        {/* Stats Cards */}
                        <div
                            className="bg-gradient-to-br from-purple-600/20 to-pink-600/20 border border-purple-500/30 rounded-xl p-6"
                            data-oid="8e3mdvc"
                        >
                            <div
                                className="flex items-center justify-between mb-4"
                                data-oid="5__2nit"
                            >
                                <h3 className="text-lg font-medium" data-oid="26ve--i">
                                    Active Agents
                                </h3>
                                <div
                                    className="w-2 h-2 bg-green-400 rounded-full animate-pulse"
                                    data-oid="q.3y:he"
                                ></div>
                            </div>
                            <div className="text-3xl font-bold mb-2" data-oid="svv75m9">
                                24
                            </div>
                            <div className="text-sm text-green-400" data-oid="v0q:.l.">
                                +12% from last week
                            </div>
                        </div>

                        <div
                            className="bg-gradient-to-br from-blue-600/20 to-cyan-600/20 border border-blue-500/30 rounded-xl p-6"
                            data-oid="vd1kta5"
                        >
                            <div
                                className="flex items-center justify-between mb-4"
                                data-oid="429he25"
                            >
                                <h3 className="text-lg font-medium" data-oid="sm4mey8">
                                    Tasks Completed
                                </h3>
                                <div
                                    className="w-2 h-2 bg-blue-400 rounded-full"
                                    data-oid="23glef0"
                                ></div>
                            </div>
                            <div className="text-3xl font-bold mb-2" data-oid="dpl_q67">
                                1,247
                            </div>
                            <div className="text-sm text-blue-400" data-oid="eljx7s_">
                                +8% efficiency
                            </div>
                        </div>

                        <div
                            className="bg-gradient-to-br from-orange-600/20 to-red-600/20 border border-orange-500/30 rounded-xl p-6"
                            data-oid="ikxsfl4"
                        >
                            <div
                                className="flex items-center justify-between mb-4"
                                data-oid="6k02i2y"
                            >
                                <h3 className="text-lg font-medium" data-oid="7nipf9t">
                                    Response Time
                                </h3>
                                <div
                                    className="w-2 h-2 bg-orange-400 rounded-full"
                                    data-oid=".bwkev-"
                                ></div>
                            </div>
                            <div className="text-3xl font-bold mb-2" data-oid="p6e:4s0">
                                0.3s
                            </div>
                            <div className="text-sm text-orange-400" data-oid="_hng7a8">
                                Average latency
                            </div>
                        </div>
                    </div>

                    {/* Activity Feed */}
                    <div
                        className="mt-6 bg-gray-800/30 border border-gray-700/50 rounded-xl p-6"
                        data-oid="9jr12te"
                    >
                        <h3 className="text-lg font-medium mb-4" data-oid="48t23d.">
                            Recent Activity
                        </h3>
                        <div className="space-y-3" data-oid="pbpyo8b">
                            {[
                                {
                                    agent: 'Agent-001',
                                    action: 'Completed data analysis task',
                                    time: '2 min ago',
                                    status: 'success',
                                },
                                {
                                    agent: 'Agent-007',
                                    action: 'Started web scraping job',
                                    time: '5 min ago',
                                    status: 'active',
                                },
                                {
                                    agent: 'Agent-003',
                                    action: 'Generated report summary',
                                    time: '12 min ago',
                                    status: 'success',
                                },
                                {
                                    agent: 'Agent-012',
                                    action: 'Waiting for user input',
                                    time: '18 min ago',
                                    status: 'pending',
                                },
                            ].map((activity, index) => (
                                <div
                                    key={index}
                                    className="flex items-center justify-between py-2 border-b border-gray-700/30 last:border-b-0"
                                    data-oid="v5hiucj"
                                >
                                    <div className="flex items-center space-x-3" data-oid="lgdt4qk">
                                        <div
                                            className={`w-2 h-2 rounded-full ${
                                                activity.status === 'success'
                                                    ? 'bg-green-400'
                                                    : activity.status === 'active'
                                                      ? 'bg-blue-400 animate-pulse'
                                                      : 'bg-yellow-400'
                                            }`}
                                            data-oid="t8ct77v"
                                        ></div>
                                        <div data-oid="y-k:0o7">
                                            <div className="font-medium" data-oid="twswk72">
                                                {activity.agent}
                                            </div>
                                            <div
                                                className="text-sm text-gray-400"
                                                data-oid="o5i4of-"
                                            >
                                                {activity.action}
                                            </div>
                                        </div>
                                    </div>
                                    <div className="text-sm text-gray-500" data-oid=":.:rnau">
                                        {activity.time}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="max-w-7xl mx-auto px-6 py-20" data-oid="py6ar51">
                <div className="text-center mb-16" data-oid="bquqaa-">
                    <h2 className="text-4xl font-bold mb-4" data-oid="ysmdyf1">
                        Powerful Features
                    </h2>
                    <p className="text-xl text-gray-300" data-oid="brsu:vb">
                        Everything you need to manage your AI agents
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-8" data-oid="nux_b6e">
                    {[
                        {
                            title: 'Real-time Monitoring',
                            description:
                                'Track agent performance and status in real-time with live updates and notifications.',
                            icon: '📊',
                        },
                        {
                            title: 'Smart Analytics',
                            description:
                                'Get insights into agent behavior, efficiency metrics, and optimization recommendations.',
                            icon: '🧠',
                        },
                        {
                            title: 'Easy Management',
                            description:
                                'Deploy, configure, and manage multiple agents from a single, intuitive interface.',
                            icon: '⚙️',
                        },
                    ].map((feature, index) => (
                        <div
                            key={index}
                            className="bg-black/40 backdrop-blur-sm border border-purple-800/30 rounded-xl p-8 hover:border-purple-600/50 transition-all"
                            data-oid="tgqm.sd"
                        >
                            <div className="text-4xl mb-4" data-oid="lyr.x5f">
                                {feature.icon}
                            </div>
                            <h3 className="text-xl font-semibold mb-3" data-oid="w5rv-08">
                                {feature.title}
                            </h3>
                            <p className="text-gray-300" data-oid="tvla67f">
                                {feature.description}
                            </p>
                        </div>
                    ))}
                </div>
            </section>

            {/* Footer */}
            <footer
                className="border-t border-purple-800/30 bg-black/20 backdrop-blur-sm"
                data-oid="ec_iz75"
            >
                <div className="max-w-7xl mx-auto px-6 py-12" data-oid="1:2.log">
                    <div className="text-center" data-oid="7e:r8d3">
                        <div
                            className="flex items-center justify-center space-x-2 mb-4"
                            data-oid="_kix7fy"
                        >
                            <div
                                className="w-8 h-8 bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg flex items-center justify-center"
                                data-oid="u07mk6f"
                            >
                                <span className="text-white font-bold text-sm" data-oid="9j9ycb4">
                                    AI
                                </span>
                            </div>
                            <span className="text-xl font-semibold" data-oid=".t9_y9v">
                                AgentPro
                            </span>
                        </div>
                        <p className="text-gray-400" data-oid="u:g3wus">
                            © 2024 AgentPro. All rights reserved.
                        </p>
                    </div>
                </div>
            </footer>
        </div>
    );
}
