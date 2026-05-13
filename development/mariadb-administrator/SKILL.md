---
name: mariadb-administrator
description: Administer and tune MariaDB systems. Use for installation, performance tuning, replication setup, backup/recovery, and security hardening.
---

# MariaDB Administrator

## Description
A skill for administering, tuning, and operating MariaDB systems, including configuration, replication, backup/recovery, monitoring, and security.

## Priority Rules
Prioritize in this order when trade-offs conflict:
1. Data integrity and backup reliability
2. Security and access control
3. Query performance
4. High availability

## When to Use
- Installing and configuring MariaDB
- Tuning performance for production workloads
- Setting up replication or clustering
- Planning and testing backup/recovery
- Investigating slow queries
- Migrating from MySQL to MariaDB
- Managing users, permissions, and hardening

## Instructions
1. **Configure server** - tune `my.cnf` for workload and hardware
2. **Tune InnoDB** - buffer pool, logs, and thread settings
3. **Analyze slow queries** - enable and review slow query log
4. **Optimize indexes** - target common filters and joins
5. **Set replication** - primary-replica or Galera for HA
6. **Set monitoring** - PMM/Prometheus with alerting
7. **Implement backups** - logical and physical strategies
8. **Validate recovery** - test restores regularly
9. **Patch proactively** - security and minor version updates

## Input Recovery Rules
- Assume modern MariaDB (10.6+) when version is not specified
- Ask for clarification only when replication or clustering requirements significantly affect configuration

## Constraints
- Do not skip backup testing
- Do not run as root
- Do not ignore security hardening

## MariaDB Focus Areas
- Versions: 10.5, 10.6, 11.x
- Engines: InnoDB, Aria, MyISAM
- Replication and Galera Cluster
- JSON features and window functions
- Capacity and storage planning

## Configuration and Tuning
- `innodb_buffer_pool_size`
- `innodb_log_file_size`
- `max_connections`
- `thread_cache_size`
- `table_open_cache`
- query cache policy (version dependent)

## Monitoring
- Slow query log
- PMM and Percona Toolkit
- Key metrics: QPS, latency, replication lag, buffer hit ratio

## Backup and Recovery
- `mysqldump` for logical backup
- Percona XtraBackup for hot physical backup
- Full + incremental strategy
- Point-in-Time Recovery (PITR)

## Security
- Least privilege access model
- Password and rotation policies
- SSL/TLS for data in transit
- Auditing and change traceability
