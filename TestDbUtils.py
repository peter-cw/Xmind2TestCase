from utils.db.DatabaseAccessObject import DatabaseAccessObject
from utils.yaml.YamlUtils import YamlUtils
mysql_conf = YamlUtils.read_yaml_all('./utils/db/config/mysql_conf.yml')[0]['test']
print(mysql_conf)
single_cf = mysql_conf['single']
print(single_cf)
pool_conf = mysql_conf['pool']

with DatabaseAccessObject(**single_cf) as dao:
    num = dao.cursor.execute('SHOW DATABASES;')
    result = dao.fetch_all()
    print(result)



