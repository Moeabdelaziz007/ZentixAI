{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset178 GeezaPro;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh9000\viewkind0
\pard\tqr\tx720\tqr\tx1440\tqr\tx2160\tqr\tx2880\tqr\tx3600\tqr\tx4320\tqr\tx5040\tqr\tx5760\tqr\tx6480\tqr\tx7200\tqr\tx7920\tqr\tx8640\pardirnatural\qr\partightenfactor0

\f0\fs24 \cf0 # plugin_example.py\
class Plugin:\
    """Base class for all plugins."""\
    def execute(self, inputs: dict) -> dict:\
        raise NotImplementedError\
\
\
class PluginRegistry:\
    """Registry to keep track of available plugins."""\
    _plugins = \{\}\
\
    @classmethod\
    def register(cls, name: str, plugin: Plugin) -> None:\
        cls._plugins[name] = plugin\
\
    @classmethod\
    def get(cls, name: str) -> Plugin | None:\
        return cls._plugins.get(name)\
\
\
class CalculatorPlugin(Plugin):\
    """Simple plugin that adds two numbers."""\
    def execute(self, inputs: dict) -> dict:\
        a = inputs.get("a")\
        b = inputs.get("b")\
        if a is None or b is None:\
            raise ValueError("CalculatorPlugin requires 'a' and 'b'.")\
        return \{"result": a + b\}\
\
\
class Agent:\
    """Agent that invokes registered plugins by name."""\
    def execute_plugin(self, name: str, inputs: dict) -> dict:\
        plugin = PluginRegistry.get(name)\
        if not plugin:\
            raise ValueError(f"No plugin named '\{name\}' registered.")\
        return plugin.execute(inputs)\
\
\
if __name__ == "__main__":\
    # Register the calculator plugin\
    PluginRegistry.register("calculator", CalculatorPlugin())\
\
    agent = Agent()\
    output = agent.execute_plugin("calculator", \{"a": 5, "b": 3\})\
    print(output)  # \{'result': 8\}\
}