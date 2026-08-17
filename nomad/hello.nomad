job "hello" {
  datacenters = ["dc1"]
  type        = "service"

  group "hello-group" {
    count = 1

    network {
      mode = "bridge"
    }

    task "hello-task" {
      driver = "docker"

      config {
        image = "localhost:5000/devops-intern-final:latest"
        force_pull = false
      }

      resources {
        cpu    = 100 # MHz
        memory = 128 # MB
      }
    }

    restart {
      attempts = 2
      interval = "5m"
      delay    = "15s"
      mode     = "fail"
    }
  }
}
