
import yaml
import sys
with open('_config.yml','r+') as yFile:
  yaml.warnings({'YAMLLoadWarning': False})
  yml=yaml.load(yFile,)
  if sys.argv[1]=="pack":
    baseurl="/fluid"
  else:
    baseurl=""

  yml['baseurl']=baseurl
  yFile.seek(0)
  yFile.truncate()
  yaml.dump(yml,yFile)
