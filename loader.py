import json


class Loader:
    def __init__(self, filename):
        self.SimulationConfig = dict()
        if str(filename).endswith(".json"):
            self.SimulationConfig = self._LoadDataFromJSON(filename)
        elif str(filename).endswith(".txt"):
            self.SimulationConfig = self._LoadDataFromTXT(filename)

    def _LoadDataFromJSON(self, filename: str) -> dict:
        configFile = open(filename, "r")

        data = json.loads(configFile.read())
        configFile.close()
        data["mode"] = "json"

        return data

    def _LoadDataFromTXT(self, filename: str) -> dict:
        configFile = open(filename, "r")
        rows = configFile.readlines()
        configFile.close()

        data = {"mode": "txt"}
        patterns = []

        i = 0
        for line in rows:
            if len(line) == 0:
                i += 1
                continue
            if i == 0:
                n = line.split(" ")
                if len(n) < 1:
                    break
                data["universe_size"] = int(n[0])
                i += 1
                continue
            else:
                coord = line.split(" ")
                (x, y) = coord

                patterns.append(
                    {
                        "x": int(x.rstrip().strip()),
                        "y": int(y.rstrip().strip())
                    }
                )
            i += 1

        if len(patterns) > 0:
            data["patterns"] = patterns

        return data

    def GetConfig(self) -> dict:
        return self.SimulationConfig
