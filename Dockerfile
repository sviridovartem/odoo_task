FROM odoo:11 as base
MAINTAINER Artem Sviridov <SvyrydovArtem@gmail.com>
USER odoo
COPY ./odoo.conf /etc/odoo/
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r ./requirements.txt
COPY  base_module usr/lib/python3/dist-packages/odoo/addons/


FROM base AS test
COPY  test_module usr/lib/python3/dist-packages/odoo/addons/
CMD bash -c "./entrypoint.sh odoo --test-enable --stop-after-init -d $ODOO_db -i $addon"

