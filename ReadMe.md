### Prerequisites:

- create a virtual env
  'python3 -m venv myenv'
- activate virtual environment
  'source <venv>/bin/activate' -- bash/zsh --
- install requirements
  'pip install -r requirements.txt'

### Executable

- In the top level of the project executable
  'python3 gpt3_script.py'

### create a image

- 'docker build -t <image_name> .'

### stand up container and see the results in output log

- 'docker run -d -p 8080:8080 <image:latest>'

- 'docker logs -f <container_id>'

### run as kubernetes pod & run service

- 'kubectl apply -f chatgpt.yaml'
- 'kubectl apply -f chatgpt-service.yaml'